<script>
    $(document).ready(function() {
        $('#person_form').bootstrapValidator({
            // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                firstname: {
                    validators: {
                            notEmpty: {
                            message: 'Firstname field is required'
                        }
                    }
                }
                lastname: {
                    validators: {
                            notEmpty: {
                            message: 'Lastname field is required'
                        }
                    }
                }
                birthdate: {
                    validators: {
                            notEmpty: {
                            message: 'Birthdate field is required'
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
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Edit Person </h3></div>
                <div class="panel-body">
					<form class="form-horizontal" method="post" action="/Person/update/{{Person['id']}}" id="person_form">
                        <a href="../../../Person">
                            <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                        </a>
                        <a href="/Person/update/{{Person['id']}}">
							<button type="submit" class="btn btn-success pull-right"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
						</a>
                        <h1></h1>
						<div class="form-group">
                            <label class="col-sm-2">id</label>
                            <div class="col-sm-8">
                                <h5> {{Person['id']}} </h5>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="firstname" class="col-sm-2">firstname</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="firstname" name='firstname' value="{{Person['firstname']}}"/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="lastname" class="col-sm-2">lastname</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="lastname" name='lastname' value="{{Person['lastname']}}" onkeyup='this.value=this.value.toUpperCase()'/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="birthdate" class="col-sm-2">birthdate</label>
                            <div class="col-sm-8">
                                <input class="form-control" type="date" id="birthdate" name='birthdate' value="{{Person['birthdate']}}"/>
                            </div>
                        </div>
						<a href="/Person/delete/{{Person['id']}}">
							<button type="button" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span> Delete</button>
						</a>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>