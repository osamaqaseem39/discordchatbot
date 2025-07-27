'use client';

import { useEffect, useState } from 'react';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { FaShieldAlt, FaLock, FaEye, FaUserShield, FaCookieBite, FaHandshake, FaChild, FaCalendarAlt, FaEnvelope, FaPhone } from 'react-icons/fa';

export default function PrivacyPage() {
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
      
      <section className="py-20">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          {/* Header */}
          <div className="text-center mb-16">
            <div className="flex justify-center mb-6">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center">
                <FaShieldAlt className="text-blue-600 text-2xl" />
              </div>
            </div>
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Privacy and Security Policy
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
              At Payday Express, protecting your privacy and ensuring the security of your personal and financial information is our top priority. 
              We are committed to maintaining the highest standards of confidentiality, data integrity, and responsible information handling.
            </p>
            <p className="text-lg text-gray-700 mt-4">
              This Privacy and Security Policy outlines how we collect, use, protect, and share your information when you interact with our services.
            </p>
          </div>

          {/* Policy Content */}
          <div className="bg-white rounded-2xl shadow-xl p-8 lg:p-12 space-y-12">
            
            {/* Information We Collect */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaEye className="mr-3 text-blue-600" />
                Information We Collect
              </h2>
              <p className="text-gray-700 mb-6">
                We collect information to provide you with secure, customized, and efficient financial services. 
                The types of information we collect include:
              </p>
              <div className="grid md:grid-cols-2 gap-6">
                <div className="bg-blue-50 rounded-lg p-6">
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">Personal Information</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>• Full name</li>
                    <li>• Email address</li>
                    <li>• Phone number</li>
                    <li>• Address</li>
                    <li>• Date of birth</li>
                    <li>• National ID (e.g., SIN)</li>
                  </ul>
                </div>
                <div className="bg-green-50 rounded-lg p-6">
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">Financial Information</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>• Bank account details</li>
                    <li>• Employment status</li>
                    <li>• Income level</li>
                    <li>• Credit score (when applicable)</li>
                  </ul>
                </div>
                <div className="bg-purple-50 rounded-lg p-6">
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">Loan Data</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>• Loan application history</li>
                    <li>• Repayment activity</li>
                    <li>• Peer-to-peer investment activity</li>
                  </ul>
                </div>
                <div className="bg-orange-50 rounded-lg p-6">
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">Device and Usage Data</h3>
                  <ul className="space-y-2 text-gray-700">
                    <li>• IP address</li>
                    <li>• Device information</li>
                    <li>• Browser type</li>
                    <li>• Interaction logs</li>
                    <li>• Cookies</li>
                  </ul>
                </div>
              </div>
            </div>

            {/* How We Use Your Information */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaUserShield className="mr-3 text-green-600" />
                How We Use Your Information
              </h2>
              <p className="text-gray-700 mb-6">We use your information to:</p>
              <div className="space-y-4">
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-blue-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Verify your identity and eligibility for loans or investment opportunities.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-green-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Process loan applications, disbursements, and repayments.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-purple-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Facilitate communication between borrowers and lenders.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-orange-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Provide customer support and respond to inquiries.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-red-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Improve our services through analytics and user feedback.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-indigo-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Comply with legal and regulatory obligations.</p>
                </div>
              </div>
              <div className="mt-6 p-4 bg-yellow-50 border-l-4 border-yellow-400 rounded">
                <p className="text-gray-700 font-medium">
                  <strong>Important:</strong> We do not sell or rent your personal data to any third parties.
                </p>
              </div>
            </div>

            {/* Data Security Measures */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaLock className="mr-3 text-purple-600" />
                Data Security Measures
              </h2>
              <p className="text-gray-700 mb-6">
                We implement a wide range of industry-standard technologies and procedures to protect your data:
              </p>
              <div className="grid md:grid-cols-2 gap-6">
                <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-lg p-6">
                  <h3 className="text-lg font-semibold text-gray-900 mb-3">End-to-End Encryption</h3>
                  <p className="text-gray-700">All sensitive data is encrypted both in transit (TLS/SSL) and at rest.</p>
                </div>
                <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-lg p-6">
                  <h3 className="text-lg font-semibold text-gray-900 mb-3">Secure Authentication</h3>
                  <p className="text-gray-700">Multi-factor authentication (2FA) and strong password policies safeguard your account.</p>
                </div>
                <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-lg p-6">
                  <h3 className="text-lg font-semibold text-gray-900 mb-3">Blockchain Audit Trails</h3>
                  <p className="text-gray-700">For peer-to-peer lending, blockchain ensures secure, immutable transaction records.</p>
                </div>
                <div className="bg-gradient-to-br from-orange-50 to-orange-100 rounded-lg p-6">
                  <h3 className="text-lg font-semibold text-gray-900 mb-3">Role-Based Access Control</h3>
                  <p className="text-gray-700">Only authorized personnel can access your information.</p>
                </div>
                <div className="bg-gradient-to-br from-red-50 to-red-100 rounded-lg p-6 md:col-span-2">
                  <h3 className="text-lg font-semibold text-gray-900 mb-3">Firewall and Intrusion Detection</h3>
                  <p className="text-gray-700">Advanced systems monitor for unauthorized access and vulnerabilities.</p>
                </div>
              </div>
            </div>

            {/* Cookies and Tracking Technologies */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaCookieBite className="mr-3 text-orange-600" />
                Cookies and Tracking Technologies
              </h2>
              <p className="text-gray-700">
                We use cookies and similar technologies to improve your browsing experience, remember your preferences, 
                and analyze site traffic. You can modify your browser settings to manage or disable cookies, 
                but please note that some features may not function properly without them.
              </p>
            </div>

            {/* Sharing Information with Third Parties */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaHandshake className="mr-3 text-indigo-600" />
                Sharing Information with Third Parties
              </h2>
              <p className="text-gray-700 mb-6">We may share your information with:</p>
              <div className="space-y-4">
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-blue-600 rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <p className="text-gray-700 font-medium">Regulatory Authorities</p>
                    <p className="text-gray-600 text-sm">to comply with legal requirements.</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-green-600 rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <p className="text-gray-700 font-medium">Payment Processors and financial partners</p>
                    <p className="text-gray-600 text-sm">for transaction execution.</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-purple-600 rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <p className="text-gray-700 font-medium">Credit Bureaus</p>
                    <p className="text-gray-600 text-sm">for assessing creditworthiness (with your consent).</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-orange-600 rounded-full mt-3 flex-shrink-0"></div>
                  <div>
                    <p className="text-gray-700 font-medium">Service Providers</p>
                    <p className="text-gray-600 text-sm">for hosting, analytics, and customer support, under strict confidentiality agreements.</p>
                  </div>
                </div>
              </div>
              <div className="mt-6 p-4 bg-red-50 border-l-4 border-red-400 rounded">
                <p className="text-gray-700 font-medium">
                  <strong>Important:</strong> We never share information with advertisers or unauthorized third parties.
                </p>
              </div>
            </div>

            {/* Your Rights and Choices */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaUserShield className="mr-3 text-green-600" />
                Your Rights and Choices
              </h2>
              <p className="text-gray-700 mb-6">You have the right to:</p>
              <div className="space-y-4">
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-blue-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Access or request a copy of your personal data.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-green-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Request correction or deletion of inaccurate or outdated data.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-purple-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Withdraw consent for specific uses of your information.</p>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="w-2 h-2 bg-orange-600 rounded-full mt-3 flex-shrink-0"></div>
                  <p className="text-gray-700">Opt out of promotional communications at any time.</p>
                </div>
              </div>
              <div className="mt-6 p-4 bg-blue-50 border-l-4 border-blue-400 rounded">
                <p className="text-gray-700">
                  You may contact us to exercise these rights via email at{' '}
                  <a href="mailto:privacy@paydayexpress.ca" className="text-blue-600 font-medium hover:underline">
                    privacy@paydayexpress.ca
                  </a>
                </p>
              </div>
            </div>

            {/* Children's Privacy */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaChild className="mr-3 text-pink-600" />
                Children's Privacy
              </h2>
              <p className="text-gray-700">
                Our services are not directed to individuals under the age of 18. We do not knowingly collect or store information from children.
              </p>
            </div>

            {/* Updates to This Policy */}
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <FaCalendarAlt className="mr-3 text-indigo-600" />
                Updates to This Policy
              </h2>
              <p className="text-gray-700">
                We may update this Privacy and Security Policy periodically to reflect changes in legal requirements, 
                technology, or our services. All updates will be posted on this page with an updated effective date. 
                Please review it regularly.
              </p>
            </div>

            {/* Contact Us */}
            <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl p-8 text-white">
              <h2 className="text-3xl font-bold mb-6">Contact Us</h2>
              <p className="text-lg mb-6">
                If you have any questions or concerns about our Privacy and Security Policy or practices, please contact:
              </p>
              <div className="space-y-4">
                <div className="flex items-center space-x-4">
                  <FaUserShield className="text-2xl" />
                  <div>
                    <p className="font-semibold">Privacy Compliance Officer</p>
                    <p>Payday Express</p>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <FaEnvelope className="text-2xl" />
                  <div>
                    <p className="font-semibold">Email</p>
                    <a href="mailto:privacy@paydayexpress.ca" className="hover:underline">
                      privacy@paydayexpress.ca
                    </a>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <FaPhone className="text-2xl" />
                  <div>
                    <p className="font-semibold">Phone</p>
                    <a href="tel:+18005555626" className="hover:underline">
                      (+1) 800-555-LOAN (5626)
                    </a>
                  </div>
                </div>
              </div>
              <div className="mt-8 p-4 bg-white bg-opacity-20 rounded-lg">
                <p className="font-semibold">Effective Date: May 24, 2025</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <Footer />
    </main>
  );
} 