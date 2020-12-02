import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import RemoveRedEye from '@material-ui/icons/RemoveRedEye';
import PeopleIcon from '@material-ui/icons/People';
import ExposurePlus1Icon from '@material-ui/icons/ExposurePlus1';


export const mainListItems = (
  <div>
    <ListItem button>
      <ListItemIcon>
        <RemoveRedEye />
      </ListItemIcon>
      <ListItemText primary="Обзор" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <ExposurePlus1Icon />
      </ListItemIcon>
      <ListItemText primary="Оценки" />
    </ListItem>
  </div>
);

export const secondaryListItems = (
  <div>
    <ListSubheader inset style={{fontWeight: 'bold'}}>Полезное</ListSubheader>
    <ListItem button>
      <ListItemIcon>
        <PeopleIcon />
      </ListItemIcon>
      <ListItemText primary="Наши Учителя" />
    </ListItem>
  </div>
);