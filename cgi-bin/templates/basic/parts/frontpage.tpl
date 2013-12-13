test123
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
<a href="?{{link view="admin}}">Backend</a>

