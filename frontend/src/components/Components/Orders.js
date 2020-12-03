import React, {useEffect, useState} from 'react';
import Link from '@material-ui/core/Link';
import axios from 'axios';
import _ from 'lodash';
import Moment from 'react-moment';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';
import TableFooter from "@material-ui/core/TableFooter";
import TablePagination from "@material-ui/core/TablePagination";
import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import {Button} from "@material-ui/core";
import TextField from "@material-ui/core/TextField";


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
    const [grades, setGrades] = useState([]);
    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(10);

    const [selectedSubj, setSelectedSubj] = useState('');
    const [selectedMark, setSelectedMark] = useState(0);


    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
    };


    useEffect(() => {
        axios.get('/api/grades')
            .then(function (response) {
                // console.log(response.data);
                // const groupedBySubj = _.groupBy(response.data, 'subject.name');
                // console.log(groupedBySubj);
                setGrades(response.data);
            })
    }, [])

    const handleFiltering = () => {
        const filter_query = {};
        if (selectedSubj)
            filter_query['subject__name'] = selectedSubj
        if (selectedMark)
            filter_query['mark__gte'] = selectedMark

        axios.get('/api/grades-filtered/', {
            params: filter_query
        })
            .then(function (response) {
                setPage(0);
                setGrades(response.data);
            })
    }



  const classes = useStyles();
  return (
    <React.Fragment>
       <div>
           <FormControl style={{width: 250, margin: 20}}>
               <InputLabel>Предмет</InputLabel>
               <Select
                   value={selectedSubj}
                   onChange={(e) => setSelectedSubj(e.target.value)}
               >
                   <MenuItem disabled value={''}>Нет</MenuItem>
                   <MenuItem value={'Математика'}>Математика</MenuItem>
                   <MenuItem value={'Физика'}>Физика</MenuItem>
                   <MenuItem value={'Украинский язык'}>Украинский язык</MenuItem>
                   <MenuItem value={'Иностранный язык'}>Иностранный язык</MenuItem>
                   <MenuItem value={'Программирование'}>Программирование</MenuItem>
               </Select>
           </FormControl>

           <TextField style={{margin: 20}} label="Оценка больше чем" variant="outlined" value={selectedMark} onChange={(e) => setSelectedMark(e.target.value)} />

           <Button variant="contained" color="primary" onClick={handleFiltering} style={{marginLeft: 20, marginTop: 30}}>
               Применить фильтры
           </Button>
       </div>

      <Title>Последние оценки</Title>
      <Table style={{overflowY: 'hidden', height: '110%'}}>
        <TableHead>
          <TableRow>
            <TableCell className={classes.bold}>Дата</TableCell>
            <TableCell className={classes.bold}>Предмет</TableCell>
            <TableCell className={classes.bold}>Ученик</TableCell>
            <TableCell className={classes.bold} align="right">Балл</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {
              (grades.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
          ).map((row, id) => (
            <TableRow key={id}>
                <TableCell><Moment format={'DD/MM/YYYY'}>{row.date}</Moment></TableCell>
              <TableCell>{row.subject.name}</TableCell>
              <TableCell>{`${row.pupil.last_name} ${row.pupil.first_name}`}</TableCell>
              <TableCell align="right" className={classes.bold}>{row.mark}</TableCell>
            </TableRow>
          ))}
        </TableBody>
          <TableFooter>
              <TableRow>
                  <TablePagination
                      rowsPerPageOptions={[10, 20, 50, {label: 'All', value: -1}]}
                      colSpan={3}
                      count={grades.length}
                      rowsPerPage={rowsPerPage}
                      page={page}
                      SelectProps={{
                          inputProps: {'aria-label': 'rows per page'},
                          native: true,
                      }}
                      onChangePage={handleChangePage}
                      onChangeRowsPerPage={handleChangeRowsPerPage}
                  />
              </TableRow>
          </TableFooter>
      </Table>
    </React.Fragment>
  );
}