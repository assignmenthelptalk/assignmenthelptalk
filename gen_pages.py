import json
import os
import re

with open('page_content.json', encoding='utf-8') as f:
    data = json.load(f)

def clean(text):
    if not text:
        return ''
    text = text.replace('\u2019', "'").replace('\u2018', "'")
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2013', '–').replace('\u2014', '—')
    text = text.replace('\u00a0', ' ').replace('\ufffd', '')
    # Escape HTML-unsafe chars
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # But fix back escaped quotes for astro props (we handle separately)
    text = re.sub(r'[\x80-\x9f]', '', text)
    return text.strip()

def render_content(items):
    lines = []
    skip_first_h1 = True
    open_section = False

    for item in items:
        tag = item['tag']
        text = clean(item['text'])

        if not text:
            continue

        if tag == 'h1':
            if skip_first_h1:
                skip_first_h1 = False
                continue
            if open_section:
                lines.append('    </section>')
            lines.append(f'    <h1 class="text-3xl font-bold text-dark mb-4">{text}</h1>')
            open_section = False

        elif tag == 'h2':
            if open_section:
                lines.append('    </section>')
            lines.append(f'    <section class="mb-8">')
            lines.append(f'      <h2 class="text-2xl font-bold text-dark mb-4">{text}</h2>')
            open_section = True

        elif tag == 'h3':
            lines.append(f'      <h3 class="text-xl font-semibold text-dark mb-3 mt-6">{text}</h3>')

        elif tag == 'h4':
            lines.append(f'      <h4 class="text-lg font-semibold text-dark mb-2 mt-4">{text}</h4>')

        elif tag == 'p':
            lines.append(f'      <p class="text-gray-700 mb-4">{text}</p>')

        elif tag in ('ul', 'ol'):
            list_items = item.get('items', [])
            if not list_items:
                continue
            list_tag = tag
            list_class = 'list-disc' if tag == 'ul' else 'list-decimal'
            lines.append(f'      <{list_tag} class="{list_class} pl-6 mb-4 space-y-1">')
            for li in list_items:
                li_text = clean(li)
                if li_text:
                    lines.append(f'        <li class="text-gray-700">{li_text}</li>')
            lines.append(f'      </{list_tag}>')

    if open_section:
        lines.append('    </section>')

    return '\n'.join(lines)

pages = [
    {
        'file': 'src/pages/index.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Assignment Help For Students From Assignment Experts',
        'description': 'Hire The Best Personal Assignment Writer Today. Assignment writing service for someone who needs to see the perfect results fast. Place An Order Now! Trusted by 100,000+ happy customers.',
        'canonical': 'https://assignmenthelptalk.com/',
        'h1': 'Hire The Best Personal Assignment Writer Today',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'index',
    },
    {
        'file': 'src/pages/order-now.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Order Now - Assignment Help Talk',
        'description': 'Place your order with Assignment Help Talk. Get professional assignment writing help from our expert writers. Fast, reliable, and plagiarism-free.',
        'canonical': 'https://assignmenthelptalk.com/order-now/',
        'h1': 'Order Now',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'order-now',
    },
    {
        'file': 'src/pages/about-us.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'About US - Assignment Help Talk',
        'description': 'Assignment Help Talk is a professional writing platform that connects talented writers with everyone who needs assignment help writing services.',
        'canonical': 'https://assignmenthelptalk.com/about-us/',
        'h1': 'Quality Service – Satisfied Customer',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'about-us',
    },
    {
        'file': 'src/pages/contact.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Contact - Assignment Help Talk',
        'description': 'Dear Customers, if you have any questions regarding our service or order, contact us directly in chat below. Our Customer Support Team is here 24/7 to help and answer any questions you might have.',
        'canonical': 'https://assignmenthelptalk.com/contact/',
        'h1': 'Contact Us',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'contact',
        'extra_content': '''    <section class="mb-8">
      <h2 class="text-2xl font-bold text-dark mb-4">Get In Touch</h2>
      <div class="bg-gray-50 rounded-xl p-8 space-y-4">
        <p class="text-gray-700"><strong>Email:</strong> <a href="mailto:support@assignmenthelptalk.com" class="text-primary hover:underline">support@assignmenthelptalk.com</a></p>
        <p class="text-gray-700"><strong>Phone:</strong> +(44) 731-183-9056</p>
        <p class="text-gray-700">Our Customer Support Team is available <strong>24/7</strong> to help and answer any questions you might have.</p>
      </div>
    </section>''',
    },
    {
        'file': 'src/pages/economics-paper-writing-services.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Economics Paper Writing Service | Best Economics Essay Help',
        'description': 'We offer top-notch economics paper writing service for students. Our team of experts will provide you with the best possible economic essay writing service.',
        'canonical': 'https://assignmenthelptalk.com/economics-paper-writing-services/',
        'h1': 'Get Economics Paper Writing Service From The Experts',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'economics-paper-writing',
    },
    {
        'file': 'src/pages/biology-paper-writing-service.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Biology Paper Writing Service | Biology Homework Help',
        'description': "We offer High quality biology paper writing service that assures you of scoring high marks will provide whether it's essays, dissertations, lab reports, or term papers.",
        'canonical': 'https://assignmenthelptalk.com/biology-paper-writing-service/',
        'h1': 'Get Biology Paper Writing Service From Experts',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'biology-paper-writing',
    },
    {
        'file': 'src/pages/nursing-paper-writing-services.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Nursing Paper Writing Help | Top Nursing Assignment Writers',
        'description': 'We are here to provide you with nursing paper writing help. Our writers have mastered the art of writing extensively-researched papers. We offer 24/7 support.',
        'canonical': 'https://assignmenthelptalk.com/nursing-paper-writing-services/',
        'h1': 'Get Nursing Paper Writing Help From Top Assignment Writers Online',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'nursing-paper-writing',
    },
    {
        'file': 'src/pages/manage-operational-plan-assignment-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Manage Operational Plan Assignment Help',
        'description': 'Get in touch with us and we will provide you with the best manage operational plan Assignment Help. We have a team of experts who can handle any type of manage operational plan assignment.',
        'canonical': 'https://assignmenthelptalk.com/manage-operational-plan-assignment-help/',
        'h1': 'Manage Operational Plan Assignment Help',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'manage-operational-plan',
    },
    {
        'file': 'src/pages/nursing-care-plan-writing-services.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Nursing Care Plan Writing Services | Nursing Care Plan Assignment Help',
        'description': 'Are you looking for Nursing Care Plan Writing Service? We offer professional nursing care plan writing services. Our writers are qualified nurses with experience writing care plans.',
        'canonical': 'https://assignmenthelptalk.com/nursing-care-plan-writing-services/',
        'h1': 'Nursing Care Plan Writing Service \u2013 Care Plan Assignment Help',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'nursing-care-plan',
    },
    {
        'file': 'src/pages/cipd-assignment-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'CIPD Assignment Help For Level 3, 5, 7 | Get 30% OFF',
        'description': 'Our CIPD assignment help in Saudi Arabia, UAE, UK, and the US is done by a team of Professional CIPD assignment writers trained in levels 3, 5, and 7.',
        'canonical': 'https://assignmenthelptalk.com/cipd-assignment-help/',
        'h1': 'Get Professional CIPD Assignment Help From Experts',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'cipd-assignment',
    },
    {
        'file': 'src/pages/nursing-capstone-project-ideas.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': '150 Nursing Capstone Project Ideas For MSN, DNP Capstones',
        'description': 'The primary objective of this article is to assist nursing students in brainstorming and exploring a wide range of nursing capstone project ideas by offering a comprehensive list of topics.',
        'canonical': 'https://assignmenthelptalk.com/nursing-capstone-project-ideas/',
        'h1': '200 Nursing Capstone Project Ideas For MSN, DNP & BSN Capstones',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'nursing-capstone-ideas',
    },
    {
        'file': 'src/pages/hr-assignment-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'HR Assignment Help From Experts UK & USA | Assignment Help Talk',
        'description': 'Order now for the best HR assignment help from our experienced team of writers. We offer a wide range of HR assignment writing services to students in the UK and USA.',
        'canonical': 'https://assignmenthelptalk.com/hr-assignment-help/',
        'h1': 'Get HR Assignment Help From Human Resources Experts UK & the USA',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'hr-assignment',
    },
    {
        'file': 'src/pages/sop-writing-services.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'SOP Writing Help Services | Best SOP Writers',
        'description': 'The Statement of Purpose (SOP) is one of the essential parts of any admission application to any institution of higher learning. Get expert SOP writing help from our professional writers.',
        'canonical': 'https://assignmenthelptalk.com/sop-writing-services/',
        'h1': 'Best SOP Writing Help Services',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'sop-writing',
    },
    {
        'file': 'src/pages/lab-report-writing-services.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Custom Lab Report Writing Service For Biology, Chemistry, Physics',
        'description': 'We are assignment writing services online company that offer top-notch lab report writing services. Lab reports are assignments based on experiments done in laboratories.',
        'canonical': 'https://assignmenthelptalk.com/lab-report-writing-services/',
        'h1': 'Lab Reports Writing Help',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'lab-report-writing',
    },
    {
        'file': 'src/pages/cips-assignment-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'CIPS Assignment Help KSA | CIPS Homework Help Dubai, UAE',
        'description': "We offer top-notch CIPS assignment help writing services for students in KSA, UAE. Our team of experts will provide you with the best possible assistance, whether it's Supply chain governance, Risk analysis, or Diligent procurement.",
        'canonical': 'https://assignmenthelptalk.com/cips-assignment-help/',
        'h1': 'Get CIPS Assignment Help From Our CIPS Assignment Writing Service',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'cips-assignment',
    },
    {
        'file': 'src/pages/gis-assignment-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'GIS Assignment Help | ArcGIS Assignment | GIS homework Help',
        'description': 'Are you looking for GIS assignment help? Our team of experienced GIS experts will take care of all your GIS assignments. Whether it is ArcGIS, QGIS, or any other GIS software, we can help.',
        'canonical': 'https://assignmenthelptalk.com/gis-assignment-help/',
        'h1': 'GIS Assignment Help & ArcGIS Homework Help',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'gis-assignment',
    },
    {
        'file': 'src/pages/dnp-capstone-project-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'DNP Capstone Project Help: From Stress to Success',
        'description': 'Struggling with your DNP capstone project? Our expert writers provide comprehensive DNP capstone project help to guide you from stress to success.',
        'canonical': 'https://assignmenthelptalk.com/dnp-capstone-project-help/',
        'h1': 'DNP Capstone Project Help: From Stress to Success',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'dnp-capstone',
    },
    {
        'file': 'src/pages/capstone-project-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Capstone Project Help From Experienced Capstone Writers',
        'description': 'Custom Capstone Project Help Writing Service from expert writers with 24/7 Support and On-Time Delivery, 100% Plagiarism Free is our guarantee for all clients.',
        'canonical': 'https://assignmenthelptalk.com/capstone-project-help/',
        'h1': 'Capstone Project Help From Experienced Capstone Writers',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'capstone-project',
    },
    {
        'file': 'src/pages/information-technology-capstone-project-ideas.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Information Technology Capstone Project Ideas',
        'description': 'However, you will require taking a unique project to do this, something most students find difficult to find unique Information Technology Capstone Project ideas. We provide a list of the best IT capstone project ideas.',
        'canonical': 'https://assignmenthelptalk.com/information-technology-capstone-project-ideas/',
        'h1': 'Information Technology Capstone Project Ideas',
        'ogImage': 'https://assignmenthelptalk.com/wp-content/uploads/2020/12/Information-Technology-Capstone-Project-Ideas-2-1.jpg',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'it-capstone-ideas',
    },
    {
        'file': 'src/pages/ilm-assignment-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Get ILM Assignment Help From ILM Experts | Level 2 to 7',
        'description': 'Get in touch with us and we will provide you with the best ILM Assignment Help. We have a team of ILM experts who are qualified to handle any type of ILM assignment.',
        'canonical': 'https://assignmenthelptalk.com/ilm-assignment-help/',
        'h1': 'Get ILM Assignment Help Online From ILM Experts',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'ilm-assignment',
    },
    {
        'file': 'src/pages/finance-assignment-help.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Finance Assignment Help | Financial Accounting Homeweork Writers',
        'description': "Our team of finance experts will help you with finance assignment help. We will take care of everything, and you don't need to worry about issues such as formatting, referencing, or plagiarism.",
        'canonical': 'https://assignmenthelptalk.com/finance-assignment-help/',
        'h1': 'Get Finance Assignment Help from Our Finance Assignment Writing Service',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'finance-assignment',
    },
    {
        'file': 'src/pages/nursing-capstone.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Nursing Writing Services Topics - AssignmentHelpTalk',
        'description': 'Check out some of our helpful posts and guides about Nursing writing services topics, capstone projects, care plans, and more.',
        'canonical': 'https://assignmenthelptalk.com/nursing-capstone/',
        'h1': 'Nursing Writing Services Topics',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'nursing-capstone',
        'extra_content': '''    <section class="mb-8">
      <h2 class="text-2xl font-bold text-dark mb-6">Nursing Writing Resources</h2>
      <div class="grid md:grid-cols-2 gap-4">
        <a href="/nursing-paper-writing-services/" class="block p-5 rounded-xl border border-gray-200 hover:border-primary hover:shadow-md transition-all">
          <h3 class="font-semibold text-primary mb-1">Nursing Paper Writing Services</h3>
          <p class="text-sm text-gray-600">Expert nursing paper writing help from qualified writers.</p>
        </a>
        <a href="/nursing-care-plan-writing-services/" class="block p-5 rounded-xl border border-gray-200 hover:border-primary hover:shadow-md transition-all">
          <h3 class="font-semibold text-primary mb-1">Nursing Care Plan Writing Services</h3>
          <p class="text-sm text-gray-600">Professional nursing care plan writing by qualified nurses.</p>
        </a>
        <a href="/nursing-capstone-project-ideas/" class="block p-5 rounded-xl border border-gray-200 hover:border-primary hover:shadow-md transition-all">
          <h3 class="font-semibold text-primary mb-1">Nursing Capstone Project Ideas</h3>
          <p class="text-sm text-gray-600">200+ nursing capstone project ideas for MSN, DNP & BSN.</p>
        </a>
        <a href="/dnp-capstone-project-help/" class="block p-5 rounded-xl border border-gray-200 hover:border-primary hover:shadow-md transition-all">
          <h3 class="font-semibold text-primary mb-1">DNP Capstone Project Help</h3>
          <p class="text-sm text-gray-600">From stress to success with expert DNP capstone support.</p>
        </a>
      </div>
    </section>''',
    },
    {
        'file': 'src/pages/business-capstone-project.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'Business Capstone Project Help From Expert Writers',
        'description': 'Are looking for a business capstone project help? We have a team of experienced business capstone project writers who can help you with your project from start to finish.',
        'canonical': 'https://assignmenthelptalk.com/business-capstone-project/',
        'h1': 'Get Business Capstone Project Help From Expert Capstone Writers',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'business-capstone',
    },
    {
        'file': 'src/pages/how-to-write-an-economics-research-paper.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'How to Write an Economics Research Paper - AssignmentHelpTalk',
        'description': 'If you are an Economics student, you are familiar with writing an economics research paper. This guide walks you through every step of the process.',
        'canonical': 'https://assignmenthelptalk.com/how-to-write-an-economics-research-paper/',
        'h1': 'How to Write an Economics Research Paper',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'economics-research-paper',
    },
    {
        'file': 'src/pages/dnp-editing-services.astro',
        'layout_import': "import BaseLayout from '../layouts/BaseLayout.astro';",
        'title': 'DNP Editing Services From Experts Editors | Edit My DNP Project',
        'description': "You've been working on your DNP project for months and now it's time to submit. Our professional DNP editing services will ensure your project is polished and ready to submit.",
        'canonical': 'https://assignmenthelptalk.com/dnp-editing-services/',
        'h1': 'Order Professional DNP Editing Services',
        'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
        'content_key': 'dnp-editing',
    },
]

BASE = os.getcwd()

created = 0
for page in pages:
    content_key = page['content_key']
    items = data.get(content_key, [])
    content_html = render_content(items)

    og_image_prop = ''
    if 'ogImage' in page:
        og_image_prop = f'\n  ogImage="{page["ogImage"]}"'

    robots_prop = f'\n  robots="{page["robots"]}"'

    title_escaped = page['title'].replace('"', '&quot;')
    desc_escaped = page['description'].replace('"', '&quot;')

    extra = page.get('extra_content', '')

    # Determine layout import depth
    depth = page['file'].count('/') - 1  # src/pages = 1 level, src/pages/order = 2 levels
    if depth == 1:
        layout_path = '../layouts/BaseLayout.astro'
        cta_path = '../components/CTAButton.astro'
    elif depth == 2:
        layout_path = '../../layouts/BaseLayout.astro'
        cta_path = '../../components/CTAButton.astro'
    else:
        layout_path = '../layouts/BaseLayout.astro'
        cta_path = '../components/CTAButton.astro'

    h1_text = page['h1'].replace('"', '&quot;')

    astro = f'''---
import BaseLayout from '{layout_path}';
import CTAButton from '{cta_path}';
---
<BaseLayout
  title="{title_escaped}"
  description="{desc_escaped}"
  canonical="{page['canonical']}"{og_image_prop}{robots_prop}
>
  <article class="container mx-auto px-4 py-12 max-w-4xl">
    <h1 class="text-4xl font-extrabold text-dark mb-6">{h1_text}</h1>

    <div class="mb-8">
      <CTAButton text="Place Your Order Now" href="/order-now/" />
    </div>

{content_html}
{extra}
    <div class="mt-12 text-center">
      <CTAButton text="Get Expert Help Now" href="/order-now/" />
    </div>
  </article>
</BaseLayout>
'''

    filepath = os.path.join(BASE, page['file'])
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(astro)
    created += 1

print(f"Created {created} page files")
