import React from 'react';
import Link from '@material-ui/core/Link';
import axios from 'axios';
import _ from 'lodash';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';

// Generate Data
function createData(id, date, subject, theme, amount) {
  return { id, date, subject, theme, amount };
}

const rows = [
  createData(0, '6 Ноя, 2020',  'Зарубежная литература', 'Барокко в литературе', 10),
  createData(1, '4 Ноя, 2020',  'Алгебра', 'Вхождение в интегралы', 8),
  createData(2, '30 Окт, 2020',  'Русский язык', 'Склонения', 11),
  createData(3, '28 Окт, 2020',  'Биология', 'Митоз', 9),
  createData(4, '26 Окт, 2020',  'Физика', 'Закон Гей-Люсака', 12),
];

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
  bold: {
    fontWeight: 'bold'
  }
}));

export default function Orders() {

  axios.get('/api/grades')
    .then(function (response) {
      console.log(response.data);

      const groupedBySubj = _.groupBy(response.data, 'subject.name');

      console.log(groupedBySubj);
      console.log(groupedBySubjAndPupil);
    })

  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Последние оценки</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell className={classes.bold}>Дата</TableCell>
            <TableCell className={classes.bold}>Предмет</TableCell>
            <TableCell className={classes.bold}>Тема</TableCell>
            <TableCell className={classes.bold} align="right">Балл</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.subject}</TableCell>
              <TableCell>{row.theme}</TableCell>
              <TableCell align="right" className={classes.bold}>{row.amount}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div className={classes.seeMore}>
        <Link color="primary" href="#" onClick={preventDefault} >
          Полный список
        </Link>
      </div>
    </React.Fragment>
  );
}