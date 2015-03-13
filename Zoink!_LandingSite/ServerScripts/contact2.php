<?php
echo 
'<!DOCTYPE html>

<html>
<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8">
	<title>Zoink! - Checkout</title>
	
<link rel="stylesheet" type="text/css" href="Zoink.css" />
	
</head>

<body>
<div id="page">';

$User_FirstName =$_POST['FirstName'];
$User_LastName = $_POST['LastName'];
$User_email = $_POST['email'];
$User_Address = $_POST['address'];
$User_City = $_POST['City'];
$User_State = $_POST['State'];
$User_ZipCode = $_POST['ZipCode'];



if($User_FirstName == 'First Name') 
	$FName_Error = "First name needs to be filled out <br>"; 
else 
	$FName = 1;	
	
if ($User_LastName == 'Last Name')
	$LName_Error = "Last name needs to be filled out <br>"; 
else
	$LName = 1;
	
if(EmailValidation($User_email)==false)
	$Email_Error =  "Not a valid email <br>"; 
else
	$Email = 1;

if ($User_Address == 'Street Address')	
	$Address_Error =  "Street address needs to be filled out <br>"; 
else 
	$Address = 1;

if ($User_City == 'City')	
	$City_Error = "City needs to be filled out <br>"; 
else
	$City = 1;

if ($User_State == 'State')	
	$State_Error =  "State needs to be filled out <br>"; 
elseif (strlen($User_State) != 2)
	$State_Error =  "Not a valid State Code... Enter as i.e. MI <br>";
else
	$State = 1;

if(validateUSAZip($User_ZipCode)==false) 
	$Zip_Error = "Not a valid 5 digit Zip Code <br>"; 
else 
	$Zip = 1;


if($FName + $LName + $Email + $Address + $City + $State + $Zip != 7)
   echo '<div id = "checkout"> <p class = "title"> It looks like there were some problems with your submission.  Please go back and correct the following: </p> <br><br>
         
         <p class = "paragraph">' . $FName_Error . $LName_Error . $Email_Error . $Address_Error . $City_Error .  $State_Error .  $Zip_Error. '</p> </div>' ;
         
else 
    table_insert($User_FirstName, $User_LastName, $User_email, $User_Address, $User_City, $User_State, $User_ZipCode);        


echo '</div> </body> </html>';

function table_insert($User_FirstName, $User_LastName, $User_email, $User_Address, $User_City, $User_State, $User_ZipCode)
{
	$con = mysql_connect("localhost","zoinkgad_admin","Zoink4ever!");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("zoinkgad_customer", $con);

$sql="INSERT INTO contact (FirstName, LastName, email, StreetAddress, City, State, ZipCode)
VALUES
('$User_FirstName','$User_LastName','$User_email', '$User_Address', '$User_City', '$User_State', '$User_ZipCode')";

if (!mysql_query($sql,$con))
  {
  die('Error: ' . mysql_error());
  }
echo '<div id = "checkout"> <p class = "title"> Thank you for signing up!  Please proceed to PayPal to complete your transaction. <br> <br> </p>
      
     <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
	 <input type="hidden" name="cmd" value="_s-xclick">
	 <input type="hidden" name="hosted_button_id" value="6AH9XAZ4BAQ2E">
	 <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
 	 <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
	 </form>

      
      </div>';
     

mysql_close($con);
}



function EmailValidation($email) { 

        $email = htmlspecialchars(stripslashes(strip_tags($email))); //parse unnecessary characters to prevent exploits

        

        if ( eregi ( '[a-z||0-9]@[a-z||0-9].[a-z]', $email ) ) { //checks to make sure the email address is in a valid format

        $domain = explode( "@", $email ); //get the domain name

                

                if ( @fsockopen ($domain[1],80,$errno,$errstr,3)) {

                        //if the connection can be established, the email address is probabley valid

                        return true;

                        /*

                        

                        GENERATE A VERIFICATION EMAIL

                        

                        */

                        

                } else {

                        return false; //if a connection cannot be established return false

                }

        

        } else {

                return false; //if email address is an invalid format return false

        }

}

function validateUSAZip($zip_code)
{
  if(preg_match("/^([0-9]{5})(-[0-9]{4})?$/i",$zip_code))
    return true;
  else
	return false;
}






?>