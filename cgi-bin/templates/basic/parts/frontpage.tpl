{{heading}}
{{var}}
<ul>
{{iterate=testit as iter}}
 <li>
  <ol>
    {{iterate=iter as i}}
     <li>{{i}}</li>
    {{/iterate}}
  </ol>
 </li>
{{/iterate}}
</ul>


