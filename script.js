// Firebase imports and config
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyCZdRSHu_rHOmeP-Y6lgFoaTvQiJrRgzYg",
  authDomain: "towardingreqform.firebaseapp.com",
  projectId: "towardingreqform",
  storageBucket: "towardingreqform.firebasestorage.app",
  messagingSenderId: "641484304227",
  appId: "1:641484304227:web:8e1176d8c3bc500e9e6d56",
  measurementId: "G-L21NMYL0XK"
};

let db = null;
try {
  if (firebaseConfig.apiKey !== "YOUR_API_KEY") {
    const app = initializeApp(firebaseConfig);
    db = getFirestore(app);
  }
} catch (err) {
  console.error("Firebase init failed:", err);
}

/* ==========================================================================
   Towarding Web Design - Main Script File
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  
  // 1. Header Scrolled Effect
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // 2. Hamburger Mobile Navigation Toggle
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
  });

  // Close menu when clicking link
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
    });
  });

  // 3. Active Nav Link on Scroll
  const sections = document.querySelectorAll('section[id]');
  window.addEventListener('scroll', () => {
    let scrollY = window.pageYOffset;
    
    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 100;
      const sectionId = current.getAttribute('id');
      
      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        document.querySelector('.nav-menu a[href*=' + sectionId + ']')?.classList.add('active');
      } else {
        document.querySelector('.nav-menu a[href*=' + sectionId + ']')?.classList.remove('active');
      }
    });
  });

  // 4. Resource Tab Switch Logic
  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.getAttribute('data-tab');
      
      // Toggle button active states
      tabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      // Toggle content panel active states
      tabContents.forEach(content => {
        content.classList.remove('active');
        if (content.id === `${tabId}-tab`) {
          content.classList.add('active');
        }
      });
    });
  });

  // 5. FAQ Accordion Logic
  const faqQuestions = document.querySelectorAll('.faq-question');
  
  faqQuestions.forEach(q => {
    q.addEventListener('click', () => {
      const faqItem = q.parentElement;
      const isActive = faqItem.classList.contains('active');
      
      // Close all first
      document.querySelectorAll('.faq-item').forEach(item => {
        item.classList.remove('active');
        item.querySelector('.faq-answer').style.maxHeight = null;
      });
      
      // Open if it wasn't active
      if (!isActive) {
        faqItem.classList.add('active');
        const answer = faqItem.querySelector('.faq-answer');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // 6. Contact Form & Modal Feedback Logic
  const contactForm = document.getElementById('contactForm');
  const feedbackModal = document.getElementById('feedbackModal');
  const modalClose = document.getElementById('modalClose');
  const modalOkBtn = document.getElementById('modalOkBtn');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const subject = document.getElementById('subject').value;
      const message = document.getElementById('message').value;
      
      console.log('Form Submitted:', { name, email, subject, message });

      // 1. Save to Firebase Firestore if configured
      if (db) {
        addDoc(collection(db, "contact_messages"), {
          name: name,
          email: email,
          subject: subject,
          message: message,
          timestamp: serverTimestamp()
        }).then(() => {
          console.log("Saved to Firestore successfully!");
        }).catch((err) => {
          console.error("Firestore write failed:", err);
        });
      } else {
        console.log("Firebase is not configured yet. Saving skipped.");
      }

      // 2. Send email notification via EmailJS if configured
      if (typeof emailjs !== "undefined") {
        emailjs.send("service_4smsj2w", "template_vibyrp8", {
          name: name,
          email: email,
          subject: subject,
          message: message
        }, "aXx7F2PnXJ4KmhsPo").then(() => {
          console.log("Email notification sent successfully!");
        }).catch((err) => {
          console.error("EmailJS send failed:", err);
        });
      }

      // Display success modal
      feedbackModal.classList.add('active');
    });
  }

  // Close Modal functions
  const closeModal = () => {
    feedbackModal.classList.remove('active');
    if (contactForm) contactForm.reset();
  };

  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (modalOkBtn) modalOkBtn.addEventListener('click', closeModal);

  // Close modal when clicking outside modal-content
  window.addEventListener('click', (e) => {
    if (e.target === feedbackModal) {
      closeModal();
    }
  });

  // 7. Scroll Reveal Animation using Intersection Observer
  const revealElements = document.querySelectorAll('.scroll-reveal');
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-active');
        // Once revealed, no need to track again
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15, // Reveal when 15% is visible
    rootMargin: '0px 0px -50px 0px' // Offset reveal point slightly
  });

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });

  // 8. Download Intro PDF & Open in New Tab
  const downloadIntroBtn = document.getElementById('download-intro-btn');
  if (downloadIntroBtn) {
    downloadIntroBtn.addEventListener('click', () => {
      // Open PDF in a new tab/window after a tiny delay so the browser can trigger the download first
      setTimeout(() => {
        window.open('/towarding_intro.pdf', '_blank');
      }, 100);
    });
  }

});
