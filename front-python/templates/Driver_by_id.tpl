<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Show Driver</h3></div>
                <div class="panel-body">
					<a href="../../../Driver">
                        <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                    </a>
					<a href=/Driver/form/update/{{Driver['person_id']}}/{{Driver['car_id']}}>
						<button type="button" class="btn btn-info pull-right"><span class="glyphicon glyphicon-refresh"></span> Update</button>
					</a>
					<h1></h1>
					{{!footer}}
					<h1></h1>
					<table class="table table-bordered text-center">
						<tbody>
						<tr>
							<td><b>person_id</b></td>
							<td>{{Driver['person_id']}}</td>
						</tr>
						<tr>
							<td><b>car_id</b></td>
							<td>{{Driver['car_id']}}</td>
						</tr>
						<tr>
							<td><b>licence_number</b></td>
							<td>{{Driver['licence_number']}}</td>
						</tr>
						<tr>
							<td><b>licence_date</b></td>
							<td>{{Driver['licence_date']}}</td>
						</tr>
						</tbody>
					</table>
					<a href="/Driver/delete/{{Driver['person_id']}}/{{Driver['car_id']}}">
						<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
					</a>
				</div>
			</div>
		</div>
	</div>
</div>
