import "./globals.css";

export const metadata = {
  title: "Govt Schemes AI Assistant",
  description: "AI-powered Government Schemes Assistant",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-900">
        <div className="h-screen flex flex-col">
          {/* Content */}
          <main className="flex-1 overflow-hidden">{children}</main>
        </div>
      </body>
    </html>
  );
}