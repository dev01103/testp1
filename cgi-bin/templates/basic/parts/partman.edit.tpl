<form action="{{link partman_action="save" SELF}}" method="POST">
Part name<input type="text" name="part_name" value="{{part.name}}" />
Part position<input type="text" name="part_position" value="{{part.position}}" />
Published <input type="checkbox" name="published" {{published}} />
<input type="submit" value="Save" />
</form>