import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const gilroy = localFont({
  src: [
    {
      path: '../../public/fonts/gilroy/Gilroy-Regular.ttf',
      weight: '400',
      style: 'normal',
    },
    {
      path: '../../public/fonts/gilroy/Gilroy-Medium.ttf',
      weight: '500',
      style: 'normal',
    },
    {
      path: '../../public/fonts/gilroy/Gilroy-Bold.ttf',
      weight: '700',
      style: 'normal',
    },
    {
      path: '../../public/fonts/gilroy/Gilroy-SemiBold.ttf',
      weight: '600',
      style: 'normal',
    },
  ],
  variable: '--font-gilroy',
  display: 'swap',
});

export const metadata: Metadata = {
  title: "PaydayExpress.ca - Fast Online Payday Loans in Canada",
  description: "Get quick payday loans online in Canada with instant approval. Fast cash when you need it most. Apply now and get funded within 24 hours.",
  keywords: "payday loans canada, quick cash loans, online payday loans, instant approval, emergency loans canada",
};

export const viewport = {
  width: 'device-width',
  initialScale: 1,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${gilroy.variable} font-gilroy`}>{children}</body>
    </html>
  );
}
