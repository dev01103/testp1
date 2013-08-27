<table border="1">
<tr>
 <th>ID</th><th>Name</th><th>Position</th>
</tr>
{{iterate=parts as part}}
<tr>
 <td>{{part.part_id}}</td><td><a href="{{link partman_layout="edit" pid="{{part.part_id}}" SELF}}">{{part.name}}</a></td><td>{{part.position}}</td>
</tr>
{{/iterate}}

</table>