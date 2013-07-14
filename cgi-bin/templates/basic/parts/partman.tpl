{{partman_toolbar}}
<table border="1">
<tr>
 <th>ID</th><th>Name</th><th>Position</th>
</tr>
{{iterate=parts as part}}
<tr>
 <td>{{part.part_id}}</td><td>{{part.name}}</td><td>{{part.position}}</td>
</tr>
{{/iterate}}

</table>
