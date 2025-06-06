const ResumeCard = ({ resume }) => (
  <div className="p-4 bg-white rounded-xl shadow-md space-y-2">
    <h2 className="text-xl font-bold mb-2">{resume.name || 'No Name'}</h2>
    <p><strong>Email:</strong> {resume.email}</p>
    <p><strong>Phone:</strong> {resume.phone}</p>
    <p><strong>About:</strong> {resume.about}</p>
    <p><strong>Skills:</strong> {resume.skills}</p>
    <p><strong>Experience:</strong> {resume.experience}</p>
    <p><strong>Education:</strong> {resume.education}</p>
    <p><strong>Certifications:</strong> {resume.certifications}</p>
    <p><strong>Projects:</strong> {resume.projects}</p>
    <p><strong>Internships:</strong> {resume.internships}</p>
    <p><strong>Strengths:</strong> {resume.strengths}</p>
    <p><strong>Weaknesses:</strong> {resume.weaknesses}</p>
    <p><strong>GitHub:</strong> {resume.github}</p>
    <p><strong>LinkedIn:</strong> {resume.linkedin}</p>
    <p><strong>Portfolio:</strong> {resume.portfolio}</p>
  </div>
);

export default ResumeCard;
