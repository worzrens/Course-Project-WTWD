import React from 'react';
import { useTheme } from '@material-ui/core/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';
import Title from './Title';

// Generate Sales Data
function createData(time, amount) {
  return { time, amount };
}

const data = [
  createData('1', 8),
  createData('2', 10),
  createData('3', 7),
  createData('4', 12),
  createData('5', 6),
  createData('6', 10),
  createData('7', 11),
  createData('8', 9),
  createData('9', 8),
  createData('10', 11),
  createData('11', undefined),
  createData('12', undefined),
  createData('13', undefined),
  createData('14', undefined),
  createData('15', undefined),
  createData('16', undefined),
  createData('17', undefined),
  createData('18', undefined),
  createData('19', undefined),
  createData('20', undefined),
  createData('21', undefined),
  createData('22', undefined),
  createData('23', undefined),
  createData('24', undefined),
  createData('25', undefined),
  createData('26', undefined),
  createData('27', undefined),
  createData('28', undefined),
  createData('29', undefined),
  createData('30', undefined),
];

export default function Chart() {
  const theme = useTheme();

  return (
    <React.Fragment>
      <Title>Средняя успеваемость за месяц</Title>
      <ResponsiveContainer>
        <LineChart
          data={data}
          margin={{
            top: 16,
            right: 16,
            bottom: 0,
            left: 24,
          }}
        >
          <XAxis dataKey="time" stroke={theme.palette.text.secondary} />
          <YAxis stroke={theme.palette.text.secondary}>
            <Label
              angle={270}
              position="left"
              style={{ textAnchor: 'middle', fill: theme.palette.text.primary }}
            >
              Балл
            </Label>
          </YAxis>
          <Line type="monotone" dataKey="amount" stroke={theme.palette.primary.main} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </React.Fragment>
  );
}
