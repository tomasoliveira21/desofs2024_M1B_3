import React from "react";

type Trend = {
  position: number;
  name: string;
  count: number;
};

type TrendTableProps = {
  trends: Trend[];
};

function TrendTable({ trends }: TrendTableProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white rounded-lg shadow-md">
        {trends.length > 0 && (
          <thead className="bg-gray-600 text-white">
            <tr>
              <th className="px-6 py-3 text-left text-sm font-medium uppercase tracking-wider">Position</th>
              <th className="px-6 py-3 text-left text-sm font-medium uppercase tracking-wider">Name</th>
              <th className="px-6 py-3 text-left text-sm font-medium uppercase tracking-wider">Count</th>
            </tr>
          </thead>
        )}
        <tbody className="bg-gray-300 divide-y divide-gray-200">
          {trends.map((trend, index) => (
            <tr key={index} className="hover:bg-gray-100">
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-bold">{'#'+ trend.position}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{trend.name}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{trend.count}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TrendTable;
