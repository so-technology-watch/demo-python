<form class="form-horizontal" method="post" action="{{save_action}}">
	<div class="form-group">
		<label for="driver_id" class="col-sm-2">driver_id</label>
		<div class="col-sm-10">
			<input type='text' id="driver_id"  name="driver_id" value="{{driver['driver_id']}}"/>
		</div>
	</div>
	<div class="form-group">
		<label for="driver_name" class="col-sm-2">driver_name</label>
		<div class="col-sm-10">
			<input type="text" id="driver_name" name="driver_name" value="{{driver['driver_name']}}"/>
		</div>
	</div>
%if mode != 'create':
	<a href="/drivers/delete/{{driver['driver_id']}}">
		<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
	</a>
	<a href="{{save_action}}/{{driver['driver_id']}}">
		<button type="submit" class="btn btn-success"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
	</a>
% else :
	<a href="{{save_action}}">
		<button type="submit" class="btn btn-success"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
	</a>
	% end
</form>