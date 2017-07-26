<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Show Person</h3></div>
                <div class="panel-body">
					<a href="../../Person">
						<button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
					</a>
					<a href=/Person/form/update/{{Person['id']}}>
						<button type="button" class="btn btn-info pull-right"><span class="glyphicon glyphicon-refresh"></span> Update</button>
					</a>
					<h1></h1>
					{{!footer}}
					<h1></h1>
					<table class="table table-bordered text-center">
						<tbody>
						<tr>
							<td><b>id</b></td>
							<td>{{Person['id']}}</td>
						</tr>
						<tr>
							<td><b>firstname</b></td>
							<td>{{Person['firstname']}}</td>
						</tr>
						<tr>
							<td><b>lastname</b></td>
							<td>{{Person['lastname']}}</td>
						</tr>
						<tr>
							<td><b>birthdate</b></td>
							<td>{{Person['birthdate']}}</td>
						</tr>
						</tbody>
					</table>
					<a href="/Person/delete/{{Person['id']}}">
						<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
					</a>
				</div>
			</div>
		</div>
	</div>
</div>
