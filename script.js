// =========================
// SMOOTH SCROLLING
// =========================

document.querySelectorAll('.nav-links a').forEach(function(link) {

    link.addEventListener('click', function(event) {

        event.preventDefault();

        const target = document.querySelector(
            this.getAttribute('href')
        );

        if (target) {

            target.scrollIntoView({
                behavior: 'smooth'
            });

        }

        // Close mobile menu after clicking a link

        navLinks.classList.remove('active');

    });

});


// =========================
// MOBILE MENU
// =========================

const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', function() {

    navLinks.classList.toggle('active');

});

// =========================
// PROJECTS SCROLL ANIMATION
// =========================

const projects = document.querySelectorAll(".project-showcase");

function showProjects() {

    projects.forEach(function(project) {

        const projectPosition =
            project.getBoundingClientRect().top;

        const screenPosition =
            window.innerHeight - 100;

        if (projectPosition < screenPosition) {
            project.classList.add("show");
        }

    });

}

window.addEventListener("scroll", showProjects);

window.addEventListener("load", showProjects);


// =========================
// PROJECT BUTTON
// =========================

const projectButtons =
    document.querySelectorAll(".project-btn");

projectButtons.forEach(function(button) {

    button.addEventListener("click", function(event) {

        if (button.getAttribute("href") === "#") {

            event.preventDefault();

            alert("GitHub project link will be added soon!");

        }

    });

});

// =========================
// CONTACT FORM
// =========================

const contactForm = document.getElementById("contactForm");

if (contactForm) {

    contactForm.addEventListener("submit", function(event) {

        event.preventDefault();

        alert("Thank you! Your message has been received.");

        contactForm.reset();

    });

}