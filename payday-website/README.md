# PaydayExpress - Payday Loan Website

A modern, professional Next.js website for a payday loan company with interactive features, loan calculator, and application form.

## Features

- **Responsive Design**: Mobile-first design that works on all devices
- **Interactive Loan Calculator**: Real-time calculation of loan amounts, fees, and APR
- **Multi-step Application Form**: Professional 3-step loan application process
- **Modern UI/UX**: Clean, professional design with smooth animations
- **SEO Optimized**: Proper meta tags and semantic HTML structure
- **Accessibility**: WCAG compliant with proper focus management
- **Security Features**: Form validation and secure data handling

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Icons**: Heroicons (SVG)
- **Deployment**: Ready for Vercel, Netlify, or any hosting platform

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd paydayexpress-website
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
├── app/
│   ├── layout.tsx          # Root layout with metadata
│   ├── page.tsx            # Homepage
│   └── globals.css         # Global styles
├── components/
│   ├── Header.tsx          # Navigation header
│   ├── Hero.tsx            # Hero section
│   ├── Features.tsx        # Features and benefits
│   ├── LoanCalculator.tsx  # Interactive loan calculator
│   ├── ApplicationForm.tsx # Multi-step application form
│   └── Footer.tsx          # Footer with contact info
```

## Key Components

### Header
- Responsive navigation menu
- Mobile hamburger menu
- Call-to-action button

### Hero Section
- Compelling headline and value proposition
- Key benefits with icons
- Trust indicators
- Sample loan calculation display

### Features
- 6 key features with icons
- Step-by-step process
- Loan requirements checklist

### Loan Calculator
- Interactive slider for loan amount
- Term selection dropdown
- Real-time APR calculation
- Payment schedule display
- Important disclaimers

### Application Form
- 3-step wizard interface
- Personal information collection
- Address and employment details
- Banking information
- Terms and conditions agreement
- Form validation

### Footer
- Company information
- Quick links
- Contact details
- Legal disclaimers
- Trust indicators

## Customization

### Colors
The website uses a blue color scheme. To change colors, update the Tailwind classes in the components or modify the `tailwind.config.js` file.

### Content
- Update text content in each component
- Modify loan amounts and terms in the calculator
- Change contact information in the footer
- Update legal disclaimers as needed

### Styling
- Custom CSS is in `src/app/globals.css`
- Tailwind classes are used throughout components
- Responsive breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px)

## Legal Compliance

The website includes:
- APR disclosures
- State restrictions notices
- Credit impact warnings
- Licensing information
- Terms and conditions links
- Privacy policy references

**Important**: This is a demo website. For production use, ensure compliance with all applicable lending laws and regulations in your jurisdiction.

## Deployment

### Vercel (Recommended)
1. Push code to GitHub
2. Connect repository to Vercel
3. Deploy automatically

### Other Platforms
The website can be deployed to any platform that supports Next.js:
- Netlify
- AWS Amplify
- DigitalOcean App Platform
- Railway

## Performance

- Optimized images and assets
- Lazy loading for better performance
- Minimal bundle size
- Fast loading times

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and demonstration purposes. Please ensure compliance with all applicable laws and regulations before using in production.

## Support

For questions or support, please contact the development team.

---

**Disclaimer**: This website is for demonstration purposes only. Payday loans have high interest rates and fees. Consider all alternatives before borrowing. Always read and understand the terms and conditions before applying for any loan.
