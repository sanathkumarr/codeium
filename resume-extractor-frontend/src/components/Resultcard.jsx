import React from 'react';

const ResultCard = ({ data }) => {
  if (!data) return null;

  const renderSection = (title, content) => (
    content ? (
      <div className="mb-4">
        <h2 className="text-xl font-semibold text-gray-800 mb-1">{title}</h2>
        {Array.isArray(content) ? (
          <ul className="flex flex-wrap gap-2">
            {content.map((item, idx) => (
              <li key={idx} className="bg-blue-100 text-blue-700 px-2 py-1 rounded-md text-sm">
                {item}
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-700 whitespace-pre-line">{content}</p>
        )}
      </div>
    ) : null
  );

  return (
    <div className="bg-white shadow-xl rounded-xl p-6 mt-6 w-full max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold text-center text-indigo-600 mb-4">Extracted Resume Information</h1>

      {renderSection("Name", data.name)}
      {renderSection("Email", data.email)}
      {renderSection("Phone", data.phone)}
      {renderSection("GitHub", data.github)}
      {renderSection("LinkedIn", data.linkedin)}
      {renderSection("Portfolio", data.portfolio)}
      {renderSection("About Me", data.about)}
      {renderSection("Skills", data.skills)}
      {renderSection("Experience", data.experience)}
      {renderSection("Internships", data.internships)}
      {renderSection("Education", data.education)}
      {renderSection("Certifications", data.certifications)}
      {renderSection("Projects", data.projects)}
      {renderSection("Strengths", data.strengths)}
      {renderSection("Weaknesses", data.weaknesses)}
    </div>
  );
};

export default ResultCard;
