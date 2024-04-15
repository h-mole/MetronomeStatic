unsigned int call_procedure();

int handle_error_demo()
{
    int __error_code, __error_line;
    {
        // if (0 != (__error_code = (int)(call_procedure())))
        if (0 != __error_code )
        {
            do
            {
                __error_line = 10;
                goto onErr;
            } while (0);
            __error_code = 1;
        }
    }

onErr:
    return __error_code;
}