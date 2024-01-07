"""email template"""


class SplitBillNotificationTemplate:
    """split bill notification template"""
    subject = """Split Bill Notification"""

    body = """
            <!DOCTYPE html>
            <html>
                  <head>
                      <title>Split bill</title>
                  </head>
                  
                  <body style="background-color: #F7F7F7;font-family: arial;padding-top: 30px;">
                      <center>
                        <div> <br />
                            {dynamic_body}
                        </div>
                      </center>
                  </body>
            </html>
            """.replace("\n", "")

