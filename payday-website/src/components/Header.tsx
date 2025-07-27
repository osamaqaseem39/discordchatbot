'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import Image from 'next/image';

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className="bg-white border-b border-gray-200 fixed top-0 left-0 right-0 z-50">
      <div className="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
        <div className={`flex justify-between items-center transition-all duration-300 ${isScrolled ? 'py-3' : 'py-6'}`}>
          {/* Logo */}
          <div className="flex items-center">
            <Link href="/" className="flex items-center space-x-2">
              <Image
                src="/images/logo.png"
                alt="PaydayExpress Logo"
                width={isScrolled ? 240 : 400}
                height={isScrolled ? 60 : 100}
                className={`w-auto transition-all duration-300 ${isScrolled ? 'h-12' : 'h-20'}`}
              />
            </Link>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex space-x-8">
            <Link href="/" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Home
            </Link>
            <Link href="#loans" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Loans
            </Link>
            <Link href="#partners" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Partners
            </Link>
            <Link href="#lending-types" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Lending Types
            </Link>
            <Link href="#payday-express" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Payday Express
            </Link>
            <Link href="#career" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Career
            </Link>
            <Link href="/contact" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Contact
            </Link>
            <Link href="/privacy" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Privacy
            </Link>
            <Link href="/partners" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              Partners
            </Link>
            <Link href="/about" className="text-gray-900 hover:text-gray-600 transition-colors font-medium">
              About
            </Link>
          </nav>

          {/* CTA Buttons */}
          <div className="hidden md:flex items-center space-x-4">
            <Link
              href="#signin"
              className="bg-white text-gray-900 px-6 py-2 rounded-lg border border-gray-300 hover:bg-gray-50 transition-colors font-medium"
            >
              Sign in
            </Link>
            <Link
              href="#apply"
              className="bg-gray-900 text-green-500 px-6 py-2 rounded-lg hover:bg-gray-800 transition-colors font-medium"
            >
              Apply now
            </Link>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="text-gray-700 hover:text-gray-600 focus:outline-none"
            >
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                {isMenuOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white border-t">
              <Link
                href="#home"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Home
              </Link>
              <Link
                href="#loans"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Loans
              </Link>
              <Link
                href="#partners"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Partners
              </Link>
              <Link
                href="#lending-types"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Lending Types
              </Link>
              <Link
                href="#payday-express"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Payday Express
              </Link>
              <Link
                href="#career"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Career
              </Link>
              <Link
                href="/contact"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Contact
              </Link>
              <Link
                href="/privacy"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Privacy
              </Link>
              <Link
                href="/partners"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                Partners
              </Link>
              <Link
                href="/about"
                className="block px-3 py-2 text-gray-900 hover:text-gray-600 transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                About
              </Link>
              <div className="px-3 py-2 space-y-2">
                <Link
                  href="#signin"
                  className="block bg-white text-gray-900 px-6 py-2 rounded-lg border border-gray-300 hover:bg-gray-50 transition-colors text-center"
                  onClick={() => setIsMenuOpen(false)}
                >
                  Sign in
                </Link>
                <Link
                  href="#apply"
                  className="block bg-gray-900 text-green-500 px-6 py-2 rounded-lg hover:bg-gray-800 transition-colors text-center"
                  onClick={() => setIsMenuOpen(false)}
                >
                  Apply now
                </Link>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  );
} 