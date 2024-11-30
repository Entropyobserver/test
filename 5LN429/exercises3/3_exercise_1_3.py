import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const CharFrequencyVisualization = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [charFreq, setCharFreq] = useState({});
  const [isComplete, setIsComplete] = useState(false);

  const myString = "This is a sentence that I have not constructed myself but I could have.";

  useEffect(() => {
    if (currentIndex < myString.length) {
      const timer = setTimeout(() => {
        setCharFreq(prev => {
          const char = myString[currentIndex];
          return { ...prev, [char]: (prev[char] || 0) + 1 };
        });
        setCurrentIndex(prev => prev + 1);
      }, 500);
      return () => clearTimeout(timer);
    } else {
      setIsComplete(true);
    }
  }, [currentIndex]);

  const data = Object.entries(charFreq).map(([char, freq]) => ({ char, freq }));

  return (
    <div className="p-4 space-y-4">
      <h2 className="text-2xl font-bold">Character Frequency Calculation Process</h2>
      <p className="text-lg">String: "{myString}"</p>
      <p className="text-lg">Current progress: {currentIndex} / {myString.length}</p>
      <div className="bg-gray-100 p-4 rounded">
        <p className="font-mono">
          {myString.split('').map((char, index) => (
            <span key={index} className={index < currentIndex ? "text-blue-600" : "text-gray-400"}>
              {char}
            </span>
          ))}
        </p>
      </div>
      <div className="bg-gray-100 p-4 rounded">
        <pre className="whitespace-pre-wrap">{JSON.stringify(charFreq, null, 2)}</pre>
      </div>
      {isComplete && (
        <>
          <p className="text-lg">String length: {myString.length}</p>
          <p className="text-lg">Unique characters: {Object.keys(charFreq).length}</p>
          <p className="text-lg">Type of char_freq: {typeof charFreq}</p>
        </>
      )}
      <div className="h-80 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <XAxis dataKey="char" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="freq" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default CharFrequencyVisualization;