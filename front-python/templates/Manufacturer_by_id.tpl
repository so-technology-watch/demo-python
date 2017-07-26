<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Show Manufacturer</h3></div>
                <div class="panel-body">
					<a href="../../Manufacturer">
						<button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
					</a>
					<a href=/Manufacturer/form/update/{{Manufacturer['id']}}>
						<button type="button" class="btn btn-info pull-right"><span class="glyphicon glyphicon-refresh"></span> Update</button>
					</a>
					<h1></h1>
					{{!footer}}
					<h1></h1>
					<table class="table table-bordered text-center">
						<tbody>
						<tr>
							<td><b>id</b></td>
							<td>{{Manufacturer['id']}}</td>
						</tr>
						<tr>
							<td><b>name</b></td>
							<td>{{Manufacturer['name']}}</td>
						</tr>
						</tbody>
					</table>
					<a href="/Manufacturer/delete/{{Manufacturer['id']}}">
						<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
					</a>
				</div>
			</div>
		</div>
	</div>
</div>
