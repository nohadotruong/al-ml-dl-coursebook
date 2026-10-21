import { Gamja_Flower } from "next/font/google";
import "./globals.css";
import ClientLayout from "./components/ClientLayout";

const gamjaFlower = Gamja_Flower({
  variable: "--font-gamja-flower",
  subsets: ["latin"],
  weight: "400",
});

export const metadata = {
  title: "AI-ML-DL Coursebook",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={`${gamjaFlower.variable} font-gamja-flower antialiased`}
      >
        <ClientLayout>{children}</ClientLayout>
      </body>
    </html>
  );
}
