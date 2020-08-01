<!DOCTYPE html>
<html>
    <head>
        <style>
            body{
                background-color: <%
                    col = Request.QueryString("Colour")
                    Response.Write(col)
                %>
            }
        </style>
    </head>
    <body>
        <h2>Lab 5</h2>
        <h2>Owen Goodwin (500909196)</h2>
        <h4>11/04/19</h4>
        <hr>
        <%
            If Request.Cookies("lastvisit") = "" Then
                Response.Write("First visit. Welcome!")
            Else
                last = Request.Cookies("lastvisit")
                Response.Write("Your last visit was: " & last)
            End if
            Response.Cookies("lastvisit") = Now
        %>
        <br>
        <%
            Response.Write("Right now, it is " & Now)
        %>
    </body>
</html>