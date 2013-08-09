test
<ul>
{{iterate=testit as iter}}
 <li>
  <ol>
    {{iterate=iter as i}}
     <li><a href="f">{{i}}</a></li>
    {{/iterate}}
  </ol>
 </li>
{{/iterate}}
</ul>
{{debug}}