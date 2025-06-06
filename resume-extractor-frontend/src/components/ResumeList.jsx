import ResumeCard from './ResumeCard';

const ResumeList = ({ resumes }) => (
  <div className="grid md:grid-cols-2 gap-6 p-4">
    {resumes.map((resume, idx) => (
      <ResumeCard key={idx} resume={resume} />
    ))}
  </div>
);

export default ResumeList;
