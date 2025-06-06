import { useState } from 'react';
import axios from 'axios';

const UploadForm = ({ onUpload }) => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);
    setLoading(true);

    try {
      const res = await axios.post('http://localhost:8000/extract', formData);
      onUpload(res.data.data);
    } catch (err) {
      alert('Upload failed. Check your backend.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col gap-4 items-center justify-center p-6 border-2 border-dashed border-gray-300 rounded-2xl shadow bg-white">
      <input
        type="file"
        onChange={e => setFile(e.target.files[0])}
        className="text-sm"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
        disabled={loading}
      >
        {loading ? 'Uploading...' : 'Upload Resume'}
      </button>
    </div>
  );
};

export default UploadForm;
