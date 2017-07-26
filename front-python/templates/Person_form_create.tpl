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
                            message: 'Fistname field is required'
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
                <div class="panel-heading"><h3><span class="glyphicon glyphicon-leaf"></span> Create Person</h3></div>
                <div class="panel-body">
                    <form class="form-horizontal" method="post" action="/Person/create" id="person_form">
                        <a href="../../../Person">
                            <button type="button" class="btn btn-warning"><span class="glyphicon glyphicon-fast-backward"></span>  Back</button>
                        </a>
                        <a href="/Person/create">
                            <button type="submit" class="btn btn-success pull-right"><span class="glyphicon glyphicon-floppy-disk"></span> Save</button>
                        </a>
                        <h1></h1>
                        <div class="form-group">
                            <label for="id" class="col-sm-2">id</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="id" name='id' value="auto value" disabled/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="firstname" class="col-sm-2">firstname</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="firstname" name='firstname' value=""/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="lastname" class="col-sm-2">lastname</label>
                            <div class="col-sm-8">
                                <input class="form-control" id="lastname" name='lastname' value="" onkeyup='this.value=this.value.toUpperCase()'/>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="birthdate" class="col-sm-2">birthdate</label>
                            <div class="col-sm-8">
                                <input class="form-control" type="date" id="birthdate" name='birthdate' value=""/>
                            </div>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</div>