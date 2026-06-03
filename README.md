# 🌐 Drift Minds Landing Page

A premium, fully responsive, and SEO-optimized landing page designed for a modern B2B apparel manufacturer. This project includes high-quality product showcase sections, an active SEO-rich blog, and standard corporate policies.

---

## 🚀 Features

- **Responsive Design:** Crafted using mobile-first best practices with smooth transitions and a modern dark/teal color scheme.
- **Product Showcase Carousels:** Dynamic interactive color variant sliders for T-shirts, Polo T-shirts, Hoodies, Sweatshirts, and Custom Caps.
- **Enquiry Form Integration:** Fully wired with EmailJS to send customer enquiries directly to your inbox.
- **SEO Blog System:** 5 comprehensive, SEO-optimized blog posts designed to rank for keywords like *"top apparel manufacturer in india"*.
- **Standard Corporate Policies:** Fully-styled templates for Privacy Policy, Refund Policy, and Terms of Service.

---

## 🛠️ Technology Stack

- **Structure & Layout:** HTML5, Tailwind CSS (via CDN)
- **Icons:** FontAwesome 6 (via CDN)
- **Form Delivery:** EmailJS (client-side email submission)
- **Images:** Premium Unsplash product templates and color-accurate assets

---

## 📂 Project Structure

```text
driftminds_landingpage/
├── assets/
│   ├── logo.png               # PNG Logo
│   └── products/              # Product image variants
├── blog/
│   ├── cotton-vs-polyester-fabric-guide.html
│   ├── custom-college-merchandise-manufacturing.html
│   ├── low-moq-clothing-manufacturing-guide.html
│   ├── sustainable-apparel-manufacturing-india.html
│   └── top-apparel-manufacturers-india.html
├── pages/
│   ├── privacy-policy.html
│   ├── refund-policy.html
│   └── terms-of-service.html
├── .gitignore
├── favicon.png
├── index.html                 # Main Landing Page
└── README.md                  # Project Documentation
```

---

## ⚙️ Configuration & Setup

### 1. Local Development
Simply open `index.html` in any modern web browser, or serve it using a lightweight dev server:
```bash
# Example using Live Server (VS Code Extension) or:
npx serve .
```

### 2. EmailJS Integration
To configure the contact/enquiry form to use your credentials:
1. Open [index.html](file:///c:/Users/DELL/Desktop/Projects/driftminds_landingpage/index.html).
2. Locate the EmailJS configuration block at the bottom of the script section:
   ```javascript
   emailjs.init("YOUR_PUBLIC_KEY");
   ```
3. Update the submission block in `handleSubmit` with your corresponding service and template ID:
   ```javascript
   emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", templateParams)
   ```
