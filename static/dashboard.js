document.addEventListener('DOMContentLoaded', function() {
    
    // Filter function 
    function filterTickets(status) {
        const cards = document.querySelectorAll('.ticket-wrapper');
        
        cards.forEach(card => {
            if (status.toLowerCase() === 'all' || card.dataset.status.toLowerCase() === status.toLowerCase()) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    const filterButtonGroup = document.getElementById('filter-btn-group');
    if (filterButtonGroup) {
        const buttons = filterButtonGroup.querySelectorAll('.btn');
        
        buttons.forEach(button => {
            button.addEventListener('click', function() {
                buttons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
                
                const filterValue = this.dataset.filter;
                filterTickets(filterValue);
            });
        });
    }

    // Calculate statistics when the page loads
    function calculateStats() {
        const ticketItems = document.querySelectorAll('.ticket-wrapper');
        let openCount = 0;
        let closedCount = 0;
        
        ticketItems.forEach(item => {
            if (item.dataset.status === 'Open') {
                openCount++;
            } else if (item.dataset.status === 'Closed') {
                closedCount++;
            }
        });

        const openCountEl = document.getElementById('open-count');
        const closedCountEl = document.getElementById('closed-count');
        if (openCountEl) openCountEl.textContent = openCount;
        if (closedCountEl) closedCountEl.textContent = closedCount;
    }
    
    // Call the function on page load if the user is an admin
    if (document.getElementById('open-count')) {
        calculateStats();
    }


    // Animation when loading the page
    const animatedCards = document.querySelectorAll('.ticket-wrapper');
    animatedCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 80);
    });
});
