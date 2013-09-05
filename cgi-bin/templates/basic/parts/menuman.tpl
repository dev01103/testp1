Menu manager
<table border="1">
<tr>
 <th>ID</th><th>Name</th>
</tr>
{{iterate=menus as m}}
<tr>
 <td>{{m.menu_id}}</td>
 <a href="{{link view="admin" menuman_layout="edit_menu"}}">tst</a> 
</tr>
{{/iterate}}

</table>
