import { Search } from 'lucide-react';
import { useState } from 'react';
import './HomePage.css';

const HomePage = () => {

  const [isModalVisible, setIsModalVisible] = useState(false);

  const toggleModal = () => {
    setIsModalVisible(!isModalVisible);
  };

  return (
    <div className="min-h-screen bg-white">

    {isModalVisible && (
            <div className={`fixed top-0 right-0 w-1/3 h-full bg-white shadow-lg z-50 transition-transform duration-300 ${isModalVisible ? 'translate-x-0' : 'translate-x-full'}`}>
              <button onClick={toggleModal} className="absolute top-4 right-4">Close</button>
              <div className="p-4">
                <h2>Profile Details</h2>
                {/* Add your modal content here */}
              </div>
            </div>
          )}

 {/* Top Blue Section */}
 <div className="bg-[#7CC5D5] rounded-b-3xl p-6 relative h-40">
        <div className="absolute top-4 right-4">

          {/* Profile Click */}
          <div id="profile" className="w-8 h-8 bg-gray-200 rounded-full hover:cursor-pointer" onClick={toggleModal}>
            <img src='https://randomuser.me/api/portraits' alt="Profile" />
          </div>
        </div>
        <h1 className="text-white text-xl mt-8">ยินดีต้อนรับ!</h1>
        
        {/* Search Bar */}
        <div className="relative mt-4">
          <input
            type="text"
            placeholder="ค้นหา"
            className="w-full p-3 rounded-lg bg-white shadow-sm"
          />
          <Search className="absolute right-3 top-3 text-gray-400" size={20} />
        </div>
      </div>

      {/* Content Section */}
      <div className="px-6 mt-6">
        <h2 className="text-sm text-gray-600 mb-4">แบบประเมินเบื้องต้น *</h2>
        
        {/* Cards Grid */}
        <div className="grid grid-cols-2 gap-4">
          {/* Lungs Assessment Card */}
          <div className="bg-gradient-to-br from-teal-50 to-teal-100 p-4 rounded-xl h-32 flex items-center justify-center">
            <div className="w-16 h-16">
              <svg viewBox="0 0 24 24" className="w-full h-full text-teal-600">
                <path
                  fill="currentColor"
                  d="M12 4c1.11 0 2 .89 2 2v4c0 1.11-.89 2-2 2s-2-.89-2-2V6c0-1.11.89-2 2-2m8 11c0 4.42-3.58 8-8 8s-8-3.58-8-8c0-3.31 2.01-6.15 4.88-7.36C10.14 7.85 10 8.4 10 9v1c-2.21 0-4 1.79-4 4 0 2.21 1.79 4 4 4s4-1.79 4-4v-1c0-.6-.14-1.15-.88-1.36C15.99 8.85 18 11.69 18 15Z"
                />
              </svg>
            </div>
          </div>

          {/* Chat Bot Card */}
          <div className="bg-gradient-to-br from-blue-50 to-blue-100 p-4 rounded-xl h-32 flex items-center justify-center">
            <div className="w-16 h-16">
              <svg viewBox="0 0 24 24" className="w-full h-full text-blue-600">
                <path
                  fill="currentColor"
                  d="M12 2a10 10 0 0 1 10 10 10 10 0 0 1-10 10c-1.97 0-3.8-.57-5.35-1.55L2 22l1.55-4.65A9.969 9.969 0 0 1 2 12 10 10 0 0 1 12 2M8 13h2v2H8v-2m4 0h2v2h-2v-2m4 0h2v2h-2v-2M8 9h2v2H8V9m4 0h2v2h-2V9m4 0h2v2h-2V9"
                />
              </svg>
            </div>
          </div>

          {/* Assessment Results Card */}
          <div className="bg-gradient-to-br from-orange-50 to-orange-100 p-4 rounded-xl h-32 flex items-center justify-center">
            <div className="w-16 h-16">
              <svg viewBox="0 0 24 24" className="w-full h-full text-orange-600">
                <path
                  fill="currentColor"
                  d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2m0 16H5V5h14v14m-7-2h2V7h-4v2h2v8Z"
                />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;