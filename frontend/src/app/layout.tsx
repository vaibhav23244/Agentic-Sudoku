import "./globals.css";
import type { Metadata } from "next";
import localFont from "next/font/local";

const grotesk = localFont({
  src: "../fonts/ClashGrotesk-Variable.ttf",
});

export const metadata: Metadata = {
  title: "AI - Sudoku Solver",
  description: "AI - Sudoku Solver",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${grotesk.className} antialiased`}>{children}</body>
    </html>
  );
}
