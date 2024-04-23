import { DataEntry } from './types';
// import { mockUploads } from '../data/mock_data';


//   export const fetchUploads = async (): Promise<Upload[]> => {
//     const response = await fetch('/api/uploads');
//     if (!response.ok) {
//       throw new Error('Failed to fetch');
//     }
//     return response.json();
//   };

export const fetchUploads = async (): Promise<DataEntry[]> => {
    return new Promise(resolve => {
      setTimeout(() => {
        const uploads = mockUploads.map(entry => ({
          ...entry,
          description: entry.abstract || "No description provided"
        }));
        resolve(uploads as DataEntry[]);
      }, 1000);
    });
  };
  
  export const approveUpload = async (id: string): Promise<void> => {
    const response = await fetch(`/api/uploads/${id}/approve`, { method: 'POST' });
    if (!response.ok) {
      throw new Error('Failed to approve');
    }
  };
  
  export const rejectUpload = async (id: string): Promise<void> => {
    const response = await fetch(`/api/uploads/${id}/reject`, { method: 'POST' });
    if (!response.ok) {
      throw new Error('Failed to reject');
    }
  };
