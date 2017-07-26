<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Show Car</h3></div>
                <div class="panel-body">
					<a href="../../Car">
						<button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
					</a>
					<a href=/Car/form/update/{{Car['id']}}>
						<button type="button" class="btn btn-info pull-right"><span class="glyphicon glyphicon-refresh"></span> Update</button>
					</a>
					<h1></h1>
					{{!footer}}
					<h1></h1>
					<table class="table table-bordered text-center">
						<tbody>
						<tr>
							<td><b>id</b></td>
							<td>{{Car['id']}}</td>
						</tr>
						<tr>
							<td><b>manufacturer_id</b></td>
							<td>{{Car['manufacturer_id']}}</td>
						</tr>
						<tr>
							<td><b>model</b></td>
							<td>{{Car['model']}}</td>
						</tr>
						<tr>
							<td><b>year</b></td>
							<td>{{Car['year']}}</td>
						</tr>
						<tr>
							<td><b>color</b></td>
							<td>{{Car['color']}}</td>
						</tr>
						</tbody>
					</table>
					<a href="/Car/delete/{{Car['id']}}">
						<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
					</a>
				</div>
			</div>
		</div>
	</div>
</div>
