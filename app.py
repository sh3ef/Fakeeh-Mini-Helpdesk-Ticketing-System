from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from functools import wraps
from config import Config
from models import User, Ticket, Reply
from flask_babel import Babel, gettext as _
# Application Configuration
app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
# Babel Configuration 
app.config['BABEL_DEFAULT_LOCALE'] = 'ar'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

def get_locale():
    if session.get('lang'):
        return session.get('lang')
    return app.config['BABEL_DEFAULT_LOCALE']

babel = Babel(app, locale_selector=get_locale)
# Language switch path
@app.route('/lang/<language>')
def set_language(language=None):
    session['lang'] = language
    return redirect(request.referrer or url_for('index'))
# Ensures that the user is logged in.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("الرجاء تسجيل الدخول أولاً", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Ensures that the user is Admin.
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("الرجاء تسجيل الدخول أولاً", "warning")
            return redirect(url_for('login'))
        if session.get("user_role") != "Admin":
            flash("ليس لديك الصلاحية للوصول لهذه الصفحة", "danger")
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function


# (App Routes) 

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.find_by_email(email)

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            flash(_("أهلاً بعودتك, %(name)s!", name=user['name']), "success")
            return redirect(url_for('dashboard'))
        else:
            flash(_('البريد الإلكتروني أو كلمة المرور غير صحيحة'), 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash(_("تم تسجيل خروجك بنجاح"), "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    if session['user_role'] == 'Admin':
        tickets = Ticket.get_all()
    else:
        tickets = Ticket.get_by_user(session['user_id'])
    return render_template('dashboard.html', tickets=tickets)

@app.route('/ticket/new', methods=['GET', 'POST'])
@login_required
def create_ticket():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if not title or not description:
            flash(_("الرجاء ملء جميع الحقول"), "danger")
            return render_template('create_ticket.html')
            
        Ticket.create(title, description, session['user_id'])
        flash(_('تم إنشاء التذكرة بنجاح'), 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_ticket.html')

@app.route('/ticket/<int:ticket_id>')
@login_required
def view_ticket(ticket_id):
    ticket = Ticket.find_by_id(ticket_id)
    
    # Check the ticket
    if not ticket:
        flash(_("التذكرة غير موجودة"), "danger")
        return redirect(url_for('dashboard'))
    
    # Ensure the user is authorized to view the ticket.
    if session['user_role'] != 'Admin' and ticket['user_id'] != session['user_id']:
        flash(_("ليس لديك الصلاحية لعرض هذه التذكرة"), "danger")
        return redirect(url_for('dashboard'))
    
    replies = Reply.get_by_ticket(ticket_id)
    return render_template('ticket_view.html', ticket=ticket, replies=replies)


@app.route('/ticket/<int:ticket_id>/reply', methods=['POST'])
@login_required
def add_reply(ticket_id):
    content = request.form.get('content')
    if not content:
        flash(_("لا يمكن إرسال رد فارغ"), "warning")
        return redirect(url_for('view_ticket', ticket_id=ticket_id))

    Reply.create(content, ticket_id, session['user_id'])
    flash(_("تم إضافة ردك بنجاح"), "success")
    return redirect(url_for('view_ticket', ticket_id=ticket_id))

@app.route('/ticket/<int:ticket_id>/close')
@admin_required
def close_ticket(ticket_id):
    Ticket.close(ticket_id)
    flash(_("تم إغلاق التذكرة بنجاح"), "info")
    return redirect(url_for('view_ticket', ticket_id=ticket_id))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
