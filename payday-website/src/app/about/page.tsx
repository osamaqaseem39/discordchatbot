'use client';

import { useEffect, useState } from 'react';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { FaHeart, FaShieldAlt, FaUsers, FaCalculator, FaHeadset, FaHandshake, FaRocket, FaCheckCircle, FaEye, FaMobile, FaNetworkWired, FaCreditCard, FaChartLine, FaGlobe } from 'react-icons/fa';

export default function AboutPage() {
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
                <FaHeart className="text-white text-2xl" />
              </div>
            </div>
            <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
              Empowering Your Financial Future —
              <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">
                Ethically, Transparently, Reliably
              </span>
            </h1>
            <p className="text-xl text-gray-600 max-w-5xl mx-auto leading-relaxed mb-8">
              At Payday Express, we're redefining how Canadians access short-term and peer-to-peer loans. 
              Our mission is clear: to provide fast, fair, and fully transparent lending solutions that meet 
              the evolving needs of modern borrowers—without hidden fees, inflated interest rates, or the 
              red tape of traditional banking.
            </p>
            <p className="text-lg text-gray-700 max-w-4xl mx-auto leading-relaxed">
              Founded with the belief that everyone deserves ethical access to capital, Payday Express combines 
              financial expertise with smart technology to deliver a lending experience that's as empowering as it is seamless.
            </p>
            <div className="mt-10">
              <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-4 rounded-lg font-semibold text-lg hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-300 shadow-lg">
                Apply Now
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Who We Are */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
                Who We Are
              </h2>
              <p className="text-lg text-gray-700 leading-relaxed mb-6">
                Payday Express is a Canadian financial technology company committed to offering alternative 
                lending solutions that are affordable, accessible, and community-driven. Whether you're 
                dealing with a temporary cash flow gap, unexpected expenses, or funding a personal project, 
                our fixed-fee loan model is designed to keep borrowing simple and stress-free.
              </p>
              <p className="text-lg text-gray-700 leading-relaxed">
                We are a team of financial experts, developers, and customer care professionals dedicated 
                to responsible lending. Backed by secure digital infrastructure and a customer-first approach, 
                we ensure every borrower feels informed, supported, and in control.
              </p>
            </div>
            <div className="bg-gradient-to-br from-blue-50 to-purple-50 rounded-2xl p-8">
              <div className="grid grid-cols-2 gap-6">
                <div className="text-center">
                  <div className="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-4">
                    <FaUsers className="text-white text-xl" />
                  </div>
                  <h3 className="font-semibold text-gray-900 mb-2">Financial Experts</h3>
                  <p className="text-sm text-gray-600">Industry professionals with decades of experience</p>
                </div>
                <div className="text-center">
                  <div className="w-16 h-16 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
                    <FaRocket className="text-white text-xl" />
                  </div>
                  <h3 className="font-semibold text-gray-900 mb-2">Developers</h3>
                  <p className="text-sm text-gray-600">Tech innovators building secure platforms</p>
                </div>
                <div className="text-center">
                  <div className="w-16 h-16 bg-purple-600 rounded-full flex items-center justify-center mx-auto mb-4">
                    <FaHeadset className="text-white text-xl" />
                  </div>
                  <h3 className="font-semibold text-gray-900 mb-2">Customer Care</h3>
                  <p className="text-sm text-gray-600">Dedicated support professionals</p>
                </div>
                <div className="text-center">
                  <div className="w-16 h-16 bg-orange-600 rounded-full flex items-center justify-center mx-auto mb-4">
                    <FaShieldAlt className="text-white text-xl" />
                  </div>
                  <h3 className="font-semibold text-gray-900 mb-2">Secure Infrastructure</h3>
                  <p className="text-sm text-gray-600">Advanced digital security systems</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* What We Offer */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              What We Offer
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Comprehensive lending solutions designed to meet your financial needs with transparency and ease.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                  <FaMobile className="text-blue-600 text-xl" />
                </div>
                <h3 className="text-xl font-bold text-gray-900">Payday Loans</h3>
              </div>
              <p className="text-gray-700">
                Quick access to short-term funds with transparent fixed fees.
              </p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mr-4">
                  <FaNetworkWired className="text-green-600 text-xl" />
                </div>
                <h3 className="text-xl font-bold text-gray-900">Peer-to-Peer Lending</h3>
              </div>
              <p className="text-gray-700">
                Borrow from real people through our secure, fully managed platform.
              </p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center mr-4">
                  <FaCreditCard className="text-purple-600 text-xl" />
                </div>
                <h3 className="text-xl font-bold text-gray-900">Personal Loans</h3>
              </div>
              <p className="text-gray-700">
                For bigger goals or longer durations—apply with ease and clear repayment plans.
              </p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center mr-4">
                  <FaCalculator className="text-orange-600 text-xl" />
                </div>
                <h3 className="text-xl font-bold text-gray-900">Financial Tools & Calculators</h3>
              </div>
              <p className="text-gray-700">
                Understand your repayment, compare fees, and plan better.
              </p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-red-100 rounded-full flex items-center justify-center mr-4">
                  <FaHeadset className="text-red-600 text-xl" />
                </div>
                <h3 className="text-xl font-bold text-gray-900">Customer Support</h3>
              </div>
              <p className="text-gray-700">
                Human-first assistance, always just a message or call away.
              </p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 bg-indigo-100 rounded-full flex items-center justify-center mr-4">
                  <FaChartLine className="text-indigo-600 text-xl" />
                </div>
                <h3 className="text-xl font-bold text-gray-900">Smart Technology</h3>
              </div>
              <p className="text-gray-700">
                AI-powered risk assessment and blockchain security for your peace of mind.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Our Approach */}
      <section className="py-20 bg-gradient-to-r from-blue-600 to-purple-600 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">Our Approach</h2>
            <p className="text-xl opacity-90 max-w-3xl mx-auto">
              Unlike traditional financial institutions, we don't believe in compounding interest or hidden penalties. 
              Instead, we offer:
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm text-center">
              <div className="w-16 h-16 bg-white bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaCalculator className="text-white text-2xl" />
              </div>
              <h3 className="text-xl font-bold mb-4">Fixed-fee structures</h3>
              <p className="opacity-90">So you know exactly what you'll pay.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm text-center">
              <div className="w-16 h-16 bg-white bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaEye className="text-white text-2xl" />
              </div>
              <h3 className="text-xl font-bold mb-4">Fast approvals</h3>
              <p className="opacity-90">With soft credit checks that protect your score.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm text-center">
              <div className="w-16 h-16 bg-white bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaHandshake className="text-white text-2xl" />
              </div>
              <h3 className="text-xl font-bold mb-4">Flexible options</h3>
              <p className="opacity-90">For short-term or mid-term lending, built around your goals.</p>
            </div>

            <div className="bg-white bg-opacity-10 rounded-2xl p-8 backdrop-blur-sm text-center">
              <div className="w-16 h-16 bg-white bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaShieldAlt className="text-white text-2xl" />
              </div>
              <h3 className="text-xl font-bold mb-4">End-to-end transparency</h3>
              <p className="opacity-90">From application to repayment.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Built for Borrowers, Trusted by Lenders */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Built for Borrowers, Trusted by Lenders
            </h2>
            <p className="text-xl text-gray-600 max-w-4xl mx-auto leading-relaxed">
              Payday Express bridges the gap between real people and real money. Our peer-to-peer lending 
              platform lets individual investors support borrowers directly—earning returns while contributing 
              to ethical finance. Borrowers get better rates, lenders enjoy full transparency, and both 
              parties benefit from a trusted environment powered by smart matching and secure processing.
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-12">
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl p-8">
              <h3 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
                <FaUsers className="mr-3 text-blue-600" />
                For Borrowers
              </h3>
              <ul className="space-y-4">
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Better rates than traditional lenders</span>
                </li>
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Transparent fee structures</span>
                </li>
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Fast approval process</span>
                </li>
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Flexible repayment options</span>
                </li>
              </ul>
            </div>

            <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-2xl p-8">
              <h3 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
                <FaHandshake className="mr-3 text-purple-600" />
                For Lenders
              </h3>
              <ul className="space-y-4">
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Predictable returns</span>
                </li>
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Full transparency</span>
                </li>
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Diversified portfolio options</span>
                </li>
                <li className="flex items-start space-x-3">
                  <FaCheckCircle className="text-green-600 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">Secure blockchain technology</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Why Choose Payday Express */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Why Choose Payday Express?
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              We're committed to providing the best lending experience with transparency and ethical practices.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaEye className="text-blue-600 text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">No Hidden Costs</h3>
              <p className="text-gray-600">What you see is what you pay.</p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaHeart className="text-green-600 text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">Ethical Lending</h3>
              <p className="text-gray-600">We prioritize fairness and borrower protection.</p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
              <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaHeadset className="text-purple-600 text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">Real-Time Support</h3>
              <p className="text-gray-600">Connect with our team whenever you need help.</p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
              <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaMobile className="text-orange-600 text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">Digital Simplicity</h3>
              <p className="text-gray-600">Apply, manage, and repay—all from your device.</p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
              <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaRocket className="text-red-600 text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">Financial Empowerment</h3>
              <p className="text-gray-600">Tools and education to help you borrow smarter.</p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
              <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <FaGlobe className="text-indigo-600 text-2xl" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">Canadian Focus</h3>
              <p className="text-gray-600">Built for Canadians, by Canadians.</p>
            </div>
          </div>
        </div>
      </section>
      
      <Footer />
    </main>
  );
} 