document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modal');
    const getStartedBtn = document.getElementById('get-started-btn');
    const closeButton = document.querySelector('.close-button');
    const cardButtons = document.querySelectorAll('.card-button');
    const nav = document.querySelector('nav');
    const userStatus = document.getElementById('userStatus');

    // Check if user is already logged in (you can modify this based on your authentication logic)
    const checkUserStatus = () => {
        const isLoggedIn = localStorage.getItem('userLoggedIn');
        if (isLoggedIn) {
            userStatus.style.display = 'flex';
        }
    };

    // Modal functionality
    function openModal() {
        modal.style.display = 'flex';
        // Use setTimeout to trigger the transition
        setTimeout(() => {
            modal.classList.add('show');
        }, 10);
        document.body.style.overflow = 'hidden';
        
        // Animate cards
        const cards = modal.querySelectorAll('.card');
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 200 + (index * 100));
        });
    }

    function closeModal() {
        modal.classList.remove('show');
        // Wait for the transition to finish before hiding the modal
        setTimeout(() => {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }, 300);
    }

    getStartedBtn.addEventListener('click', openModal);
    closeButton.addEventListener('click', closeModal);

    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Handle card buttons
    cardButtons.forEach(button => {
        button.addEventListener('click', () => {
            const action = button.getAttribute('data-action');
            if (action === 'login') {
                window.location.href = 'login-admin.html';
            } else if (action === 'verify') {
                window.location.href = 'verify.html';
            }
        });
    });

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.feature, .contact-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });

    // Parallax effect for gradient backgrounds
    window.addEventListener('mousemove', (e) => {
        const moveX = (e.clientX - window.innerWidth / 2) * 0.01;
        const moveY = (e.clientY - window.innerHeight / 2) * 0.01;
        
        document.querySelector('.hero::before').style.transform = 
            `translate(${moveX}px, ${moveY}px)`;
    });

    // Close with Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('show')) {
            closeModal();
        }
    });

    // Initialize
    checkUserStatus();
});
