<script>
    $(document).ready(function() {
        $('#manufacturer_form').bootstrapValidator({
            // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                name: {
                    validators: {
                            notEmpty: {
                            message: 'Name field is required'
                        }
                    }
                }
            }
        })
    });
</script>

<div class="container">
    <h2></h2>
    <div class="container">
        <div class="panel-group">
            <div class="panel panel-info">
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Edit Manufacturer </h3></div>
                <div class="panel-body">
					<form class="form-horizontal" method="post" action="/Manufacturer/update/{{Manufacturer['id']}}" id="manufacturer_form">
                        <a href="../../../Manufacturer">
                            <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                        </a>
                        <a href="/Manufacturer/update/{{Manufacturer['id']}}">
							<button type="submit" class="btn btn-success pull-right"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
						</a>
                        <h1></h1>
						<div class="form-group">
                            <label class="col-sm-2">id</label>
                            <div class="col-sm-8">
                                <h5> {{Manufacturer['id']}} </h5>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="name" class="col-sm-2">name</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="name" name='name' value="{{Manufacturer['name']}}"/>
                            </div>
                        </div>
						<a href="/Manufacturer/delete/{{Manufacturer['id']}}">
							<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
						</a>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>