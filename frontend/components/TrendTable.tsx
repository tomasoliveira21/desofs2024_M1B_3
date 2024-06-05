import React from "react";

type Trend = {
  position: number;
  name: string;
  count: number;
};

type TrendTableProps = {
  trends: Trend[];
};

function TrendTable({ trends }: TrendTableProps) {  return (
    <table className="table-auto w-full">
      <thead>
        <tr>
          <th className="px-4 py-2">Position</th>
          <th className="px-4 py-2">Name</th>
          <th className="px-4 py-2">Count</th>
        </tr>
      </thead>
      <tbody>
        {trends.map((trend, index) => (
          <tr key={index}>
            <td className="border px-4 py-2">{trend.position}</td>
            <td className="border px-4 py-2">{trend.name}</td>
            <td className="border px-4 py-2">{trend.count}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TrendTable;
