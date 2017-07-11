<form class="form-horizontal" method="post" action="{{save_action}}">
	<div class="form-group">
		<label for="car_id" class="col-sm-2">car_id</label>
		<div class="col-sm-8">
			<input type='text' id="car_id" name='car_id' value="{{car['car_id']}}"/>
		</div>
	</div>
	<div class="form-group">
		<label for="car_name" class="col-sm-2">car_name</label>
		<div class="col-sm-8">
			<input type="text" id="car_name" name="car_name" value="{{car['car_name']}}"/>
		</div>
	</div>
	<div class="form-group">
		<label for="driver_id" class="col-sm-2">driver_id</label>
		<div class="col-sm-8">
			<input id="driver_id"  name="driver_id" value="{{car['driver_id']}}"/>
		</div>
	</div>
%if mode != 'create':
	<a href="/cars/delete/{{car['car_id']}}">
		<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
	</a>
	<a href="{{save_action}}/{{car['car_id']}}">
		<button type="submit" class="btn btn-success"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
	</a>
% else :
	<a href="{{save_action}}">
		<button type="submit" class="btn btn-success"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
	</a>
	% end
</form>