'use client';

import { useEffect, useRef, useState } from 'react';
import Image from 'next/image';

export default function HowItWorks() {
  const [visibleCards, setVisibleCards] = useState<Set<number>>(new Set());
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const index = parseInt(entry.target.getAttribute('data-index') || '0');
          if (entry.isIntersecting) {
            setVisibleCards(prev => new Set([...prev, index]));
          }
          // Removed the else clause to prevent hiding cards when scrolling down
        });
      },
      { 
        threshold: 0.1,
        rootMargin: '0px 0px -150px 0px'
      }
    );

    // Observe all cards after they're rendered
    const cards = document.querySelectorAll('[data-index]');
    cards.forEach(card => observer.observe(card));

    return () => observer.disconnect();
  }, []);
  const steps = [
    {
      number: '01',
      title: 'Sign Up',
      description: 'Create your account in under a minute with just email and phone.',
      icon: '📱',
      image: '/images/step1.png',
      detailedText: 'Sign Up for Free\n\nCreate your Payday Express account in under a minute. All you need is your email and phone number to get started securely.',
      gradient: 'from-blue-500 to-cyan-500'
    },
    {
      number: '02',
      title: 'Complete Profile',
      description: 'Add your details and bank info securely.',
      icon: '👤',
      image: '/images/step2.png',
      detailedText: 'Complete Your Profile\n\nAdd personal details, income proof, and bank information. Your data is encrypted and used only for verification and approval.',
      gradient: 'from-purple-500 to-pink-500'
    },
    {
      number: '03',
      title: 'Choose Loan',
      description: 'Select Payday, Personal, or Peer-to-Peer loan.',
      icon: '💰',
      image: '/images/step3.png',
      detailedText: 'Choose a Loan Type\n\nSelect the loan that fits your needs—Payday Loan, Personal Loan, or Peer-to-Peer. Each comes with transparent, fixed fees and zero hidden interest.',
      gradient: 'from-green-500 to-emerald-500'
    },
    {
      number: '04',
      title: 'Apply',
      description: 'Submit your application in minutes.',
      icon: '📝',
      image: '/images/step4.png',
      detailedText: 'Apply in Minutes\n\nSubmit a short application tailored to your selected loan. No complicated paperwork, just a quick digital process.',
      gradient: 'from-orange-500 to-red-500'
    },
    {
      number: '05',
      title: 'Get Approved',
      description: 'Receive instant pre-approval with AI.',
      icon: '✅',
      image: '/images/step5.png',
      detailedText: 'Get Instant Pre-Approval\n\nOur AI-powered system evaluates your application and gives you a pre-approval decision instantly—no credit score impact.',
      gradient: 'from-indigo-500 to-blue-500'
    },
    {
      number: '06',
      title: 'Get Funds',
      description: 'Receive money in hours, not days.',
      icon: '🏦',
      image: '/images/step6.png',
      detailedText: 'Receive Your Funds\n\nOnce approved, funds are deposited directly to your bank—often within hours for payday loans.',
      gradient: 'from-teal-500 to-cyan-500'
    }
  ];



  return (
    <section ref={sectionRef} id="how-it-works" className="py-16 bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 overflow-hidden snap-y snap-mandatory">
      <div className="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h2 className="text-4xl lg:text-5xl font-bold text-gray-900 mb-4">
            How It Works — Simple, Fast, and Transparent
          </h2>
          <p className="text-xl text-gray-600 max-w-4xl mx-auto">
            Get your loan in 6 simple steps. No complicated processes, just straightforward lending.
          </p>
        </div>

        {/* Timeline */}
        <div className="relative">
          {/* Timeline Line */}
          <div className={`absolute left-1/2 transform -translate-x-px h-full w-0.5 bg-gradient-to-b from-blue-400 to-purple-400 hidden lg:block transition-all duration-1000 ${visibleCards.size > 0 ? 'opacity-100' : 'opacity-0'}`}></div>

          {/* Steps */}
          <div className="space-y-0">
            {steps.map((step, index) => (
              <div 
                key={step.number} 
                data-index={index}
                className={`relative flex items-center ${index % 2 === 0 ? 'lg:flex-row' : 'lg:flex-row-reverse'} transition-all duration-1000 snap-start min-h-[50vh]`}
                style={{ 
                  marginTop: index > 0 ? '-100px' : '0',
                  transform: visibleCards.has(index) ? 'translateX(0)' : `translateX(${index % 2 === 0 ? '-100%' : '100%'})`,
                  opacity: visibleCards.has(index) ? 1 : 0,
                  willChange: 'transform, opacity'
                }}
              >
                {/* Timeline Dot */}
                <div className={`absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-6 h-6 bg-gradient-to-r ${step.gradient} rounded-full border-4 border-white shadow-xl hidden lg:block z-10 transition-all duration-1000 ${visibleCards.has(index) ? 'scale-100' : 'scale-0'}`}></div>

                {/* Content */}
                <div className={`lg:w-1/2 ${index % 2 === 0 ? 'lg:pr-2' : 'lg:pl-2'}`}>
                  <div className="relative w-[400px] h-[500px] mx-auto group perspective-1000">
                    {/* Front of Card */}
                    <div className="absolute inset-0 bg-gradient-to-br from-white via-gray-50 to-gray-100 rounded-3xl p-6 shadow-2xl border border-gray-200 transition-all duration-700 transform-style-preserve-3d group-hover:rotate-y-180 backface-hidden hover:shadow-3xl">
                      {/* Step Number and Icon */}
                      <div className="flex items-center mb-4">
                        <div className={`w-12 h-12 bg-gradient-to-r ${step.gradient} rounded-xl flex items-center justify-center mr-3 shadow-lg`}>
                          <span className="text-white font-bold text-lg">{step.number}</span>
                        </div>
                        <div className="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center shadow-md">
                          <span className="text-2xl">{step.icon}</span>
                        </div>
                      </div>

                      {/* Step Title */}
                      <h3 className="text-2xl font-bold text-gray-900 mb-3">
                        {step.title}
                      </h3>

                      {/* Step Description */}
                      <p className="text-gray-600 leading-relaxed text-base">
                        {step.description}
                      </p>

                      {/* Step Image */}
                      <div className="mt-4 rounded-2xl overflow-hidden w-[280px] h-[280px] mx-auto bg-gradient-to-br from-gray-50 to-gray-100 p-2">
                        <Image
                          src={step.image}
                          alt={`Step ${step.number} - ${step.title}`}
                          width={280}
                          height={280}
                          className="w-full h-full object-contain rounded-xl"
                        />
                      </div>
                    </div>

                    {/* Back of Card */}
                    <div className="absolute inset-0 bg-gradient-to-br from-white via-gray-50 to-gray-100 rounded-3xl p-6 shadow-2xl border border-gray-200 transition-all duration-700 transform-style-preserve-3d rotate-y-180 group-hover:rotate-y-0 backface-hidden">
                      <div className="h-full flex flex-col justify-center">
                        <div className="text-center">
                          {/* Step number and icon on back */}
                          <div className="flex justify-center items-center mb-4">
                            <div className={`w-12 h-12 bg-gradient-to-r ${step.gradient} rounded-xl flex items-center justify-center mr-3 shadow-lg`}>
                              <span className="text-white font-bold text-lg">{step.number}</span>
                            </div>
                            <div className="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center shadow-md">
                              <span className="text-2xl">{step.icon}</span>
                            </div>
                          </div>
                          <h3 className="text-2xl font-bold text-gray-900 mb-3">
                            {step.detailedText.split('\n\n')[0]}
                          </h3>
                          <p className="text-gray-600 leading-relaxed text-base">
                            {step.detailedText.split('\n\n')[1]}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Spacer for mobile */}
                <div className="lg:hidden w-full h-8"></div>
              </div>
            ))}
          </div>
        </div>

        {/* CTA */}
        <div className="text-center mt-12">
          <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-4 rounded-xl text-lg font-semibold hover:from-blue-700 hover:to-purple-700 transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105">
            Get Started Now
          </button>
        </div>
      </div>
    </section>
  );
} 