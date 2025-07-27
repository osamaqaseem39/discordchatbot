'use client';

import { useEffect, useState } from 'react';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { FaHandshake, FaShieldAlt, FaChartLine, FaNetworkWired, FaBrain, FaMapMarkerAlt, FaCheckCircle, FaRocket, FaUsers, FaLock, FaEye, FaGlobe, FaCalculator, FaMobile, FaCreditCard, FaEnvelope } from 'react-icons/fa';

export default function PartnersPage() {
  const [scrollProgress, setScrollProgress] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (window.scrollY / totalHeight) * 100;
      setScrollProgress(progress);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 pt-16">
      {/* Scroll Progress Indicator */}
      <div 
        className="scroll-indicator" 
        style={{ width: `${scrollProgress}%` }}
      ></div>
      
      <Header />
      
      {/* Hero Section */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <div className="flex justify-center mb-6">
              <div className="w-16 h-16 bg-gradient-to-r from-blue-600 to-purple-600 rounded-full flex items-center justify-center">
                <FaHandshake className="text-white text-2xl" />
              </div>
            </div>
            <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
              Invest with Confidence:
              <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">
                Partner in Ethical Lending
              </span>
            </h1>
            <p className="text-xl text-gray-600 max-w-4xl mx-auto leading-relaxed mb-8">
              Earn predictable returns while empowering communities through transparent, fixed-fee lending backed by blockchain security.
            </p>
            <p className="text-lg text-gray-700 max-w-5xl mx-auto leading-relaxed">
              At Payday Express, we're redefining lending with transparency, fixed-fee structures, and blockchain-powered security. 
              Our platform offers a unique opportunity for investors and strategic partners to participate in a growing ethical finance 
              ecosystem that supports everyday Canadians—students, workers, families, and small business owners—by providing fair, 
              fast, and accessible loan products.
            </p>
            <div className="mt-10">
              <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-4 rounded-lg font-semibold text-lg hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-300 shadow-lg">
                Apply Now
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Simple, Secure, and Smart Loans */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Simple, Secure, and Smart Loans
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Choose from personal, payday, and P2P loans designed to fit your lifestyle. 
              Powered by smart contracts and AI for seamless, low-cost borrowing.
            </p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl p-8 text-center">
              <div className="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaUsers className="text-white text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">Personal Loans</h3>
              <p className="text-gray-600">Flexible financing for life's unexpected expenses with competitive rates and quick approval.</p>
            </div>
            <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-2xl p-8 text-center">
              <div className="w-16 h-16 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaMobile className="text-white text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">Payday Loans</h3>
              <p className="text-gray-600">Quick cash advances for urgent needs with transparent fees and fast funding.</p>
            </div>
            <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-2xl p-8 text-center">
              <div className="w-16 h-16 bg-purple-600 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaNetworkWired className="text-white text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">P2P Loans</h3>
              <p className="text-gray-600">Direct lending between individuals with blockchain security and smart contract automation.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Why Partner with Us */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Why Partner with Us?
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Trusted platform offering fixed returns, secure blockchain transactions, and transparent lending for long-term growth.
            </p>
          </div>

          <div className="grid lg:grid-cols-2 gap-12">
            {/* Fixed Fee, Transparent Returns */}
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                  <FaCalculator className="text-blue-600 text-xl" />
                </div>
                <h3 className="text-2xl font-bold text-gray-900">Fixed Fee, Transparent Returns</h3>
              </div>
              <p className="text-gray-700 leading-relaxed">
                Our model eliminates compounding interest in favor of clear, fixed fees. As an investor, 
                you know exactly what return to expect—no surprises.
              </p>
            </div>

            {/* Blockchain-Enabled Security */}
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mr-4">
                  <FaLock className="text-green-600 text-xl" />
                </div>
                <h3 className="text-2xl font-bold text-gray-900">Blockchain-Enabled Security</h3>
              </div>
              <p className="text-gray-700 leading-relaxed">
                All transactions are logged on a secure, decentralized ledger ensuring transparency, 
                traceability, and trust. Smart contracts automate processes, reducing operational risk and overhead.
              </p>
            </div>

            {/* Diversified Loan Portfolio */}
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center mr-4">
                  <FaChartLine className="text-purple-600 text-xl" />
                </div>
                <h3 className="text-2xl font-bold text-gray-900">Diversified Loan Portfolio</h3>
              </div>
              <p className="text-gray-700 leading-relaxed">
                Spread your capital across payday, peer-to-peer, and category-specific loans (like education, 
                personal, mortgage return, business, and medical) to reduce risk and increase yield stability.
              </p>
            </div>

            {/* AI-Powered Risk Assessment */}
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center mr-4">
                  <FaBrain className="text-orange-600 text-xl" />
                </div>
                <h3 className="text-2xl font-bold text-gray-900">AI-Powered Risk Assessment</h3>
              </div>
              <p className="text-gray-700 leading-relaxed">
                We use AI-driven credit evaluation tools and borrower profiling to ensure responsible lending 
                and minimize defaults. Every loan is backed by real-time data and predictive analysis.
              </p>
            </div>

            {/* Canadian Market Focus */}
            <div className="bg-white rounded-2xl shadow-xl p-8 lg:col-span-2">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-red-100 rounded-full flex items-center justify-center mr-4">
                  <FaMapMarkerAlt className="text-red-600 text-xl" />
                </div>
                <h3 className="text-2xl font-bold text-gray-900">Canadian Market Focus</h3>
              </div>
              <p className="text-gray-700 leading-relaxed">
                With a deep understanding of local compliance (FINTRAC, PIPEDA, and provincial regulations), 
                we are poised to capture a loyal, underserved lending market across Ontario, Quebec, and beyond.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Benefits to Investors */}
      <section className="py-20 bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">Benefits to Investors</h2>
            <p className="text-xl opacity-90 max-w-3xl mx-auto">
              Join our platform and enjoy these exclusive benefits designed for serious investors.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm">
              <div className="flex items-center mb-4">
                <FaCheckCircle className="text-green-400 text-2xl mr-3" />
                <h3 className="text-xl font-bold">Consistent, fixed returns</h3>
              </div>
              <p className="opacity-90">Predictable income streams with transparent fee structures.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm">
              <div className="flex items-center mb-4">
                <FaCheckCircle className="text-green-400 text-2xl mr-3" />
                <h3 className="text-xl font-bold">Portfolio risk control</h3>
              </div>
              <p className="opacity-90">Advanced tools for managing and tracking investment performance.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm">
              <div className="flex items-center mb-4">
                <FaCheckCircle className="text-green-400 text-2xl mr-3" />
                <h3 className="text-xl font-bold">Full transparency</h3>
              </div>
              <p className="opacity-90">Complete visibility via blockchain records and real-time reporting.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm">
              <div className="flex items-center mb-4">
                <FaCheckCircle className="text-green-400 text-2xl mr-3" />
                <h3 className="text-xl font-bold">Auto-matching</h3>
              </div>
              <p className="opacity-90">Intelligent pairing with vetted borrowers for optimal returns.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm">
              <div className="flex items-center mb-4">
                <FaCheckCircle className="text-green-400 text-2xl mr-3" />
                <h3 className="text-xl font-bold">Real-time dashboards</h3>
              </div>
              <p className="opacity-90">Live investment tracking and performance analytics.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm">
              <div className="flex items-center mb-4">
                <FaCheckCircle className="text-green-400 text-2xl mr-3" />
                <h3 className="text-xl font-bold">Regulatory compliance</h3>
              </div>
              <p className="opacity-90">Full compliance with Canadian financial regulations and standards.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Let's Build Ethical Finance Together */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Let's Build Ethical Finance Together
            </h2>
            <p className="text-xl text-gray-600 max-w-4xl mx-auto leading-relaxed">
              At Payday Express, we believe in profitable purpose. Our mission is not just to fund loans, 
              but to empower lives. Whether you're a private investor, a tech-focused VC, or a financial 
              institution seeking innovation, this is your chance to be part of Canada's next fintech success story.
            </p>
          </div>

          <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-3xl p-12 text-white text-center">
            <div className="flex justify-center mb-8">
              <div className="w-20 h-20 bg-white bg-opacity-20 rounded-full flex items-center justify-center">
                <FaRocket className="text-white text-3xl" />
              </div>
            </div>
            <h3 className="text-3xl font-bold mb-6">Ready to Invest or Collaborate?</h3>
            <p className="text-xl mb-8 opacity-90">
              Let's talk about how you can grow your capital and community impact with us.
            </p>
            <div className="flex items-center justify-center space-x-4 text-lg">
              <FaEnvelope className="text-2xl" />
              <a 
                href="mailto:invest@paydayexpress.ca" 
                className="font-semibold hover:underline"
              >
                invest@paydayexpress.ca
              </a>
            </div>
          </div>
        </div>
      </section>
      
      <Footer />
    </main>
  );
} 