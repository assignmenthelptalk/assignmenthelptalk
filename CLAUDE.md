# CLAUDE.md — Rebuild assignmenthelptalk.com in Astro

## Project Overview

You are rebuilding **assignmenthelptalk.com** as a static site using **Astro**.
The site is an academic writing services platform. The single most important
requirement is that **every URL, title tag, meta description, H1, H2 structure,
canonical tag, and robots directive must be preserved exactly** so that existing
Google rankings are retained during the migration.

---

## Tech Stack

- **Framework:** Astro (latest stable)
- **Styling:** Tailwind CSS
- **Deployment:** Netlify or Vercel (static output)
- **Output mode:** `output: 'static'` in astro.config.mjs
- **TypeScript:** enabled (strict mode)

---

## Critical SEO Rules (Non-Negotiable)

1. **URL structure must be identical** — trailing slashes must match exactly.
   - Pages with trailing slash: keep trailing slash (e.g. `/about-us/`)
   - Pages without trailing slash: no trailing slash (e.g. `/order/user/login`)
2. **Title tags must be copied verbatim** from the table below — do not reword.
3. **Meta descriptions must be copied verbatim** — do not reword or shorten.
4. **Canonical tags** must point to `https://assignmenthelptalk.com{slug}`
5. **Robots meta** must be `index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large` on all public pages.
6. **H1 tags must match exactly** as recorded below.
7. **H2 order and wording must match** the original page structure.
8. **Do not redirect or change any slug** — not even to add/remove a trailing slash.
9. The `<html lang="en">` attribute must be present on every page.
10. All pages must render full HTML at build time (no client-side rendering of main content).

---

## Project Structure

```
/
├── public/
│   ├── robots.txt
│   └── sitemap.xml          # must list all 27 URLs with correct trailing slashes
├── src/
│   ├── components/
│   │   ├── BaseHead.astro   # handles all <head> SEO tags
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   └── CTAButton.astro
│   ├── layouts/
│   │   └── BaseLayout.astro
│   └── pages/
│       ├── index.astro                                        # /
│       ├── order-now.astro                                    # /order-now/
│       ├── about-us.astro                                     # /about-us/
│       ├── contact.astro                                      # /contact/
│       ├── economics-paper-writing-services.astro             # /economics-paper-writing-services/
│       ├── biology-paper-writing-service.astro                # /biology-paper-writing-service/
│       ├── nursing-paper-writing-services.astro               # /nursing-paper-writing-services/
│       ├── manage-operational-plan-assignment-help.astro      # /manage-operational-plan-assignment-help/
│       ├── nursing-care-plan-writing-services.astro           # /nursing-care-plan-writing-services/
│       ├── cipd-assignment-help.astro                         # /cipd-assignment-help/
│       ├── nursing-capstone-project-ideas.astro               # /nursing-capstone-project-ideas/
│       ├── hr-assignment-help.astro                           # /hr-assignment-help/
│       ├── sop-writing-services.astro                         # /sop-writing-services/
│       ├── lab-report-writing-services.astro                  # /lab-report-writing-services/
│       ├── cips-assignment-help.astro                         # /cips-assignment-help/
│       ├── gis-assignment-help.astro                          # /gis-assignment-help/
│       ├── dnp-capstone-project-help.astro                    # /dnp-capstone-project-help/
│       ├── capstone-project-help.astro                        # /capstone-project-help/
│       ├── information-technology-capstone-project-ideas.astro# /information-technology-capstone-project-ideas/
│       ├── ilm-assignment-help.astro                          # /ilm-assignment-help/
│       ├── finance-assignment-help.astro                      # /finance-assignment-help/
│       ├── nursing-capstone.astro                             # /nursing-capstone/
│       ├── business-capstone-project.astro                    # /business-capstone-project/
│       ├── how-to-write-an-economics-research-paper.astro     # /how-to-write-an-economics-research-paper/
│       ├── dnp-editing-services.astro                         # /dnp-editing-services/
│       └── order/
│           ├── index.astro                                    # /order/
│           └── user/
│               └── login.astro                                # /order/user/login
```

---

## astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://assignmenthelptalk.com',
  trailingSlash: 'ignore',   // handle per-page manually
  integrations: [
    tailwind(),
    sitemap({
      filter: (page) => !page.includes('/order/user/login'),
    }),
  ],
  output: 'static',
});
```

---

## BaseHead.astro Component

This component handles every SEO tag. Every page MUST use it.

```astro
---
interface Props {
  title: string;
  description: string;
  canonical: string;
  ogTitle?: string;
  ogImage?: string;
  robots?: string;
}
const {
  title,
  description,
  canonical,
  ogTitle,
  ogImage = 'https://assignmenthelptalk.com/wp-content/uploads/default-og.jpg',
  robots = 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
} = Astro.props;
---
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content={description} />
<meta name="robots" content={robots} />
<link rel="canonical" href={canonical} />
<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:title" content={ogTitle ?? title} />
<meta property="og:description" content={description} />
<meta property="og:url" content={canonical} />
<meta property="og:image" content={ogImage} />
<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content={ogTitle ?? title} />
<meta name="twitter:description" content={description} />
<meta name="twitter:image" content={ogImage} />
```

---

## BaseLayout.astro

```astro
---
import BaseHead from '../components/BaseHead.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';

interface Props {
  title: string;
  description: string;
  canonical: string;
  ogTitle?: string;
  ogImage?: string;
  robots?: string;
}
const props = Astro.props;
---
<!doctype html>
<html lang="en">
  <head>
    <BaseHead {...props} />
  </head>
  <body>
    <Header />
    <main>
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

---

## Page-by-Page SEO Reference

Each entry below is the **source of truth** for that page's Astro frontmatter.
Copy these values exactly — do not paraphrase, truncate, or reformat them.

---

### Page 1 — Homepage
```
File:        src/pages/index.astro
URL:         /
Canonical:   https://assignmenthelptalk.com/
Title:       Assignment Help For Students From Assignment Experts
Description: Hire The Best Personal Assignment Writer Today. Assignment writing service for someone who needs to see the perfect results fast. Place An Order Now! Trusted by 100,000+ happy customers.
H1:          Hire The Best Personal Assignment Writer Today
H2s (order): Trusted by 100,000+ happy customers | Our Unbeatable Services | Writing | Rewriting
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 2 — Order Now
```
File:        src/pages/order-now.astro
URL:         /order-now/
Canonical:   https://assignmenthelptalk.com/order-now/
Title:       Order Now - Assignment Help Talk
Description: Place your order with Assignment Help Talk. Get professional assignment writing help from our expert writers. Fast, reliable, and plagiarism-free.
H1:          Order Now
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
Note:        Original title was "Order Now -" (site name missing). Use "Order Now - Assignment Help Talk" to complete it. Keep the page URL identical.
```

---

### Page 3 — Order User Login
```
File:        src/pages/order/user/login.astro
URL:         /order/user/login
Canonical:   https://assignmenthelptalk.com/order/user/login
Title:       Login - Assignment Help Talk
Description: Login or register to place your assignment order with Assignment Help Talk.
H1:          You must login/register to place order
Robots:      noindex, nofollow
Note:        This is a functional login page — set robots to noindex to prevent duplicate/thin content indexing.
```

---

### Page 4 — About Us
```
File:        src/pages/about-us.astro
URL:         /about-us/
Canonical:   https://assignmenthelptalk.com/about-us/
Title:       About US - Assignment Help Talk
Description: Assignment Help Talk is a professional writing platform that connects talented writers with everyone who needs assignment help writing services.
H1:          Quality Service – Satisfied Customer
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 5 — Contact
```
File:        src/pages/contact.astro
URL:         /contact/
Canonical:   https://assignmenthelptalk.com/contact/
Title:       Contact - Assignment Help Talk
Description: Dear Customers, if you have any questions regarding our service or order, contact us directly in chat below. Our Customer Support Team is here 24/7 to help and answer any questions you might have.
H1:          Contact Us
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 6 — Order
```
File:        src/pages/order/index.astro
URL:         /order/
Canonical:   https://assignmenthelptalk.com/order/
Title:       Place an Order - Assignment Help Talk
Description: Place your assignment order securely. Login or register to get started with Assignment Help Talk.
H1:          Place Your Order
Robots:      noindex, nofollow
Note:        Functional order gateway page — noindex to avoid thin content.
```

---

### Page 7 — Economics Paper Writing Services
```
File:        src/pages/economics-paper-writing-services.astro
URL:         /economics-paper-writing-services/
Canonical:   https://assignmenthelptalk.com/economics-paper-writing-services/
Title:       Economics Paper Writing Service | Best Economics Essay Help
Description: We offer top-notch economics paper writing service for students. Our team of experts will provide you with the best possible economic essay writing service.
H1:          Get Economics Paper Writing Service From The Experts
H2s (order): Economics Essay Writing Services | Why You Need Professional Economics Paper Writing Service | Types of Economics Paper Provided by Experts
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 8 — Biology Paper Writing Service
```
File:        src/pages/biology-paper-writing-service.astro
URL:         /biology-paper-writing-service/
Canonical:   https://assignmenthelptalk.com/biology-paper-writing-service/
Title:       Biology Paper Writing Service | Biology Homework Help
Description: We offer High quality biology paper writing service that assures you of scoring high marks will provide whether it's essays, dissertations, lab reports, or term papers.
H1:          Get Biology Paper Writing Service From Experts
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 9 — Nursing Paper Writing Services
```
File:        src/pages/nursing-paper-writing-services.astro
URL:         /nursing-paper-writing-services/
Canonical:   https://assignmenthelptalk.com/nursing-paper-writing-services/
Title:       Nursing Paper Writing Help | Top Nursing Assignment Writers
Description: We are here to provide you with nursing paper writing help. Our writers have mastered the art of writing extensively-researched papers. We offer 24/7 support.
H1:          Get Nursing Paper Writing Help From Top Assignment Writers Online
H2s (order): Nursing Paper Writing Help From Expert Nursing Assignment Writers | Why Choose Nursing paper Writing Services? | Things to Look for When Choosing a Nursing Paper Writing Service
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 10 — Manage Operational Plan Assignment Help
```
File:        src/pages/manage-operational-plan-assignment-help.astro
URL:         /manage-operational-plan-assignment-help/
Canonical:   https://assignmenthelptalk.com/manage-operational-plan-assignment-help/
Title:       Manage Operational Plan Assignment Help
Description: Get in touch with us and we will provide you with the best manage operational plan Assignment Help. We have a team of experts who can handle any type of manage operational plan assignment.
H1:          Manage Operational Plan Assignment Help
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 11 — Nursing Care Plan Writing Services
```
File:        src/pages/nursing-care-plan-writing-services.astro
URL:         /nursing-care-plan-writing-services/
Canonical:   https://assignmenthelptalk.com/nursing-care-plan-writing-services/
Title:       Nursing Care Plan Writing Services | Nursing Care Plan Assignment Help
Description: Are you looking for Nursing Care Plan Writing Service? We offer professional nursing care plan writing services. Our writers are qualified nurses with experience writing care plans.
H1:          Nursing Care Plan Writing Service – Care Plan Assignment Help
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 12 — CIPD Assignment Help
```
File:        src/pages/cipd-assignment-help.astro
URL:         /cipd-assignment-help/
Canonical:   https://assignmenthelptalk.com/cipd-assignment-help/
Title:       CIPD Assignment Help For Level 3, 5, 7 | Get 30% OFF
Description: Our CIPD assignment help in Saudi Arabia, UAE, UK, and the US is done by a team of Professional CIPD assignment writers trained in levels 3, 5, and 7.
H1:          Get Professional CIPD Assignment Help From Experts
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 13 — Nursing Capstone Project Ideas
```
File:        src/pages/nursing-capstone-project-ideas.astro
URL:         /nursing-capstone-project-ideas/
Canonical:   https://assignmenthelptalk.com/nursing-capstone-project-ideas/
Title:       150 Nursing Capstone Project Ideas For MSN, DNP Capstones
Description: The primary objective of this article is to assist nursing students in brainstorming and exploring a wide range of nursing capstone project ideas by offering a comprehensive list of topics.
H1:          200 Nursing Capstone Project Ideas For MSN, DNP & BSN Capstones
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
Note:        Title tag says "150" but H1 says "200" — preserve both exactly as-is, this is intentional.
```

---

### Page 14 — HR Assignment Help
```
File:        src/pages/hr-assignment-help.astro
URL:         /hr-assignment-help/
Canonical:   https://assignmenthelptalk.com/hr-assignment-help/
Title:       HR Assignment Help From Experts UK & USA | Assignment Help Talk
Description: Order now for the best HR assignment help from our experienced team of writers. We offer a wide range of HR assignment writing services to students in the UK and USA.
H1:          Get HR Assignment Help From Human Resources Experts UK & the USA
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 15 — SOP Writing Services
```
File:        src/pages/sop-writing-services.astro
URL:         /sop-writing-services/
Canonical:   https://assignmenthelptalk.com/sop-writing-services/
Title:       SOP Writing Help Services | Best SOP Writers
Description: The Statement of Purpose (SOP) is one of the essential parts of any admission application to any institution of higher learning. Get expert SOP writing help from our professional writers.
H1:          Best SOP Writing Help Services
H2s (order): How Do You Structure Your SOP? | Structure of a Statement of Purpose | Tips for Writing a Winning Statement of Purpose | Checklist for a Flawless Statement of Purpose
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 16 — Lab Report Writing Services
```
File:        src/pages/lab-report-writing-services.astro
URL:         /lab-report-writing-services/
Canonical:   https://assignmenthelptalk.com/lab-report-writing-services/
Title:       Custom Lab Report Writing Service For Biology, Chemistry, Physics
Description: We are assignment writing services online company that offer top-notch lab report writing services. Lab reports are assignments based on experiments done in laboratories.
H1:          Lab Reports Writing Help
H2s (order): Why Seek Professional Lab Report Writing Help? | Lab Report Format and Structure | Steps to writing a Successful Lab Report | Subjects that We Offer Lab Report Writing Services
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 17 — CIPS Assignment Help
```
File:        src/pages/cips-assignment-help.astro
URL:         /cips-assignment-help/
Canonical:   https://assignmenthelptalk.com/cips-assignment-help/
Title:       CIPS Assignment Help KSA | CIPS Homework Help Dubai, UAE
Description: We offer top-notch CIPS assignment help writing services for students in KSA, UAE. Our team of experts will provide you with the best possible assistance, whether it's Supply chain governance, Risk analysis, or Diligent procurement.
H1:          Get CIPS Assignment Help From Our CIPS Assignment Writing Service
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 18 — GIS Assignment Help
```
File:        src/pages/gis-assignment-help.astro
URL:         /gis-assignment-help/
Canonical:   https://assignmenthelptalk.com/gis-assignment-help/
Title:       GIS Assignment Help | ArcGIS Assignment | GIS homework Help
Description: Are you looking for GIS assignment help? Our team of experienced GIS experts will take care of all your GIS assignments. Whether it is ArcGIS, QGIS, or any other GIS software, we can help.
H1:          GIS Assignment Help & ArcGIS Homework Help
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 19 — DNP Capstone Project Help
```
File:        src/pages/dnp-capstone-project-help.astro
URL:         /dnp-capstone-project-help/
Canonical:   https://assignmenthelptalk.com/dnp-capstone-project-help/
Title:       DNP Capstone Project Help: From Stress to Success
Description: Struggling with your DNP capstone project? Our expert writers provide comprehensive DNP capstone project help to guide you from stress to success.
H1:          DNP Capstone Project Help: From Stress to Success
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 20 — Capstone Project Help
```
File:        src/pages/capstone-project-help.astro
URL:         /capstone-project-help/
Canonical:   https://assignmenthelptalk.com/capstone-project-help/
Title:       Capstone Project Help From Experienced Capstone Writers
Description: Custom Capstone Project Help Writing Service from expert writers with 24/7 Support and On-Time Delivery, 100% Plagiarism Free is our guarantee for all clients.
H1:          Capstone Project Help From Experienced Capstone Writers
H2s (order): Capstone Project Help | Types of Capstone Assignments Offered by Professionals | Externally-oriented Capstone Assignment | Practice-oriented simulations
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 21 — Information Technology Capstone Project Ideas
```
File:        src/pages/information-technology-capstone-project-ideas.astro
URL:         /information-technology-capstone-project-ideas/
Canonical:   https://assignmenthelptalk.com/information-technology-capstone-project-ideas/
Title:       Information Technology Capstone Project Ideas
Description: However, you will require taking a unique project to do this, something most students find difficult to find unique Information Technology Capstone Project ideas. We provide a list of the best IT capstone project ideas.
H1:          Information Technology Capstone Project Ideas
H2s (order): How to Choose the Best Information Technology Capstone Project Idea | What Goes Into the Best IT Capstone Project Ideas? | Outline for Information Technology Capstone Project | Guide to Writing a Perfect Information Technology Capstone Project | Tips for Writing a Winning IT Capstone Project
OG Image:    https://assignmenthelptalk.com/wp-content/uploads/2020/12/Information-Technology-Capstone-Project-Ideas-2-1.jpg
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 22 — ILM Assignment Help
```
File:        src/pages/ilm-assignment-help.astro
URL:         /ilm-assignment-help/
Canonical:   https://assignmenthelptalk.com/ilm-assignment-help/
Title:       Get ILM Assignment Help From ILM Experts | Level 2 to 7
Description: Get in touch with us and we will provide you with the best ILM Assignment Help. We have a team of ILM experts who are qualified to handle any type of ILM assignment.
H1:          Get ILM Assignment Help Online From ILM Experts
H2s (order): ILM Assignment Help | An Overview of ILM Course | ILM Assignment Help Levels by Top Assignment Service Providers | ILM Topics Offered by Online Service Providers
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 23 — Finance Assignment Help
```
File:        src/pages/finance-assignment-help.astro
URL:         /finance-assignment-help/
Canonical:   https://assignmenthelptalk.com/finance-assignment-help/
Title:       Finance Assignment Help | Financial Accounting Homeweork Writers
Description: Our team of finance experts will help you with finance assignment help. We will take care of everything, and you don't need to worry about issues such as formatting, referencing, or plagiarism.
H1:          Get Finance Assignment Help from Our Finance Assignment Writing Service
H2s (order): Finance Assignment Help | How Online Agencies Provide Students With Finance Assignment Help
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
Note:        "Homeweork" is a typo in the original title tag — preserve it exactly to avoid a title change that could affect rankings.
```

---

### Page 24 — Nursing Capstone
```
File:        src/pages/nursing-capstone.astro
URL:         /nursing-capstone/
Canonical:   https://assignmenthelptalk.com/nursing-capstone/
Title:       Nursing Writing Services Topics - AssignmentHelpTalk
Description: Check out some of our helpful posts and guides about Nursing writing services topics, capstone projects, care plans, and more.
H1:          Nursing Writing Services Topics
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 25 — Business Capstone Project
```
File:        src/pages/business-capstone-project.astro
URL:         /business-capstone-project/
Canonical:   https://assignmenthelptalk.com/business-capstone-project/
Title:       Business Capstone Project Help From Expert Writers
Description: Are looking for a business capstone project help? We have a team of experienced business capstone project writers who can help you with your project from start to finish.
H1:          Get Business Capstone Project Help From Expert Capstone Writers
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 26 — How to Write an Economics Research Paper
```
File:        src/pages/how-to-write-an-economics-research-paper.astro
URL:         /how-to-write-an-economics-research-paper/
Canonical:   https://assignmenthelptalk.com/how-to-write-an-economics-research-paper/
Title:       How to Write an Economics Research Paper - AssignmentHelpTalk
Description: If you are an Economics student, you are familiar with writing an economics research paper. This guide walks you through every step of the process.
H1:          How to Write an Economics Research Paper
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

### Page 27 — DNP Editing Services
```
File:        src/pages/dnp-editing-services.astro
URL:         /dnp-editing-services/
Canonical:   https://assignmenthelptalk.com/dnp-editing-services/
Title:       DNP Editing Services From Experts Editors | Edit My DNP Project
Description: You've been working on your DNP project for months and now it's time to submit. Our professional DNP editing services will ensure your project is polished and ready to submit.
H1:          Order Professional DNP Editing Services
Robots:      index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large
```

---

## Example Page Template

Every service page follows this pattern:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout
  title="Economics Paper Writing Service | Best Economics Essay Help"
  description="We offer top-notch economics paper writing service for students. Our team of experts will provide you with the best possible economic essay writing service."
  canonical="https://assignmenthelptalk.com/economics-paper-writing-services/"
>
  <article>
    <h1>Get Economics Paper Writing Service From The Experts</h1>
    <section>
      <h2>Economics Essay Writing Services</h2>
      <p>...</p>
    </section>
    <section>
      <h2>Why You Need Professional Economics Paper Writing Service</h2>
      <p>...</p>
    </section>
    <section>
      <h2>Types of Economics Paper Provided by Experts</h2>
      <p>...</p>
    </section>
  </article>
</BaseLayout>
```

---

## robots.txt

```
User-agent: *
Allow: /
Disallow: /order/user/login
Disallow: /order/

Sitemap: https://assignmenthelptalk.com/sitemap.xml
```

---

## sitemap.xml (manual entries — must match exactly)

The Astro sitemap integration will auto-generate most entries.
Make sure these exact URLs appear with trailing slashes where required:

```
https://assignmenthelptalk.com/
https://assignmenthelptalk.com/order-now/
https://assignmenthelptalk.com/about-us/
https://assignmenthelptalk.com/contact/
https://assignmenthelptalk.com/economics-paper-writing-services/
https://assignmenthelptalk.com/biology-paper-writing-service/
https://assignmenthelptalk.com/nursing-paper-writing-services/
https://assignmenthelptalk.com/manage-operational-plan-assignment-help/
https://assignmenthelptalk.com/nursing-care-plan-writing-services/
https://assignmenthelptalk.com/cipd-assignment-help/
https://assignmenthelptalk.com/nursing-capstone-project-ideas/
https://assignmenthelptalk.com/hr-assignment-help/
https://assignmenthelptalk.com/sop-writing-services/
https://assignmenthelptalk.com/lab-report-writing-services/
https://assignmenthelptalk.com/cips-assignment-help/
https://assignmenthelptalk.com/gis-assignment-help/
https://assignmenthelptalk.com/dnp-capstone-project-help/
https://assignmenthelptalk.com/capstone-project-help/
https://assignmenthelptalk.com/information-technology-capstone-project-ideas/
https://assignmenthelptalk.com/ilm-assignment-help/
https://assignmenthelptalk.com/finance-assignment-help/
https://assignmenthelptalk.com/nursing-capstone/
https://assignmenthelptalk.com/business-capstone-project/
https://assignmenthelptalk.com/how-to-write-an-economics-research-paper/
https://assignmenthelptalk.com/dnp-editing-services/
```
Note: /order/ and /order/user/login are excluded from sitemap.

---

## Navigation Links (Header)

Preserve these exact anchor texts and hrefs in the Header component:

| Label | href |
|-------|------|
| Home | / |
| About Us | /about-us/ |
| Order Now | /order-now/ |
| Contact | /contact/ |

---

## Internal Linking Rules (SEO)

- The homepage must link to every major service page.
- Each service page must have at least one internal link back to a related service page.
- Use descriptive anchor text that matches the target page's primary keyword.
- Do NOT use generic anchor text like "click here" or "read more".

---

## SEO Launch Checklist

Before going live, verify each of the following:

- [ ] All 27 URLs render at exactly the right path (check trailing slashes)
- [ ] Every page has a unique `<title>` tag matching the table above verbatim
- [ ] Every page has a unique `<meta name="description">` matching the table above
- [ ] Every page has a `<link rel="canonical">` pointing to the correct production URL
- [ ] Every public page has robots `index, follow` (login/order pages have `noindex`)
- [ ] H1 on every page matches the table above exactly
- [ ] H2 order on every page matches the table above
- [ ] No duplicate title tags across any two pages
- [ ] No duplicate meta descriptions across any two pages
- [ ] sitemap.xml is accessible at https://assignmenthelptalk.com/sitemap.xml
- [ ] robots.txt is accessible at https://assignmenthelptalk.com/robots.txt
- [ ] robots.txt references the sitemap URL
- [ ] `<html lang="en">` present on all pages
- [ ] Open Graph tags present on all pages
- [ ] Twitter Card tags present on all pages
- [ ] No broken internal links
- [ ] Google Search Console verified and new sitemap submitted on launch day
- [ ] 301 redirects in place if old WordPress URLs had any variations (e.g. http → https, www → non-www)
