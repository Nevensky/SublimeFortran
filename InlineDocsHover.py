import sublime
import sublime_plugin

intrinsics = [
"ABORT", "ABS", "ACCESS", "ACHAR", "ACOS", "ACOSH", "ADJUSTL", "ADJUSTR", "AIMAG", "AINT", "ALARM", "ALL", "ALLOCATED", "AND", "ANINT", "ANY", "ASIN", "ASINH", "ASSOCIATED", "ATAN", "ATAN2",
"ATANH", "ATOMIC_ADD", "ATOMIC_AND", "ATOMIC_CAS", "ATOMIC_DEFINE", "ATOMIC_FETCH_ADD", "ATOMIC_FETCH_AND", "ATOMIC_FETCH_OR", "ATOMIC_FETCH_XOR", "ATOMIC_OR", "ATOMIC_REF", "ATOMIC_XOR", "BACKTRACE", "BESSEL_J0", "BESSEL_J1", "BESSEL_JN", "BESSEL_Y0", "BESSEL_Y1", "BESSEL_YN", "BGE", "BGT",
"BIT_SIZE", "BLE", "BLT", "BTEST", "C_ASSOCIATED", "C_F_POINTER", "C_F_PROCPOINTER", "C_FUNLOC", "C_LOC", "C_SIZEOF", "CEILING", "CHAR", "CHDIR", "CHMOD", "CMPLX", "CO_BROADCAST", "CO_MAX", "CO_MIN", "CO_REDUCE", "CO_SUM", "COMMAND_ARGUMENT_COUNT",
"COMPILER_OPTIONS", "COMPILER_VERSION", "COMPLEX", "CONJG", "COS", "COSH", "COUNT", "CPU_TIME", "CSHIFT", "CTIME", "DATE_AND_TIME", "DBLE", "DCMPLX", "DIGITS", "DIM", "DOT_PRODUCT", "DPROD", "DREAL", "DSHIFTL", "DSHIFTR", "DTIME",
"EOSHIFT", "EPSILON", "ERF", "ERFC", "ERFC_SCALED", "ETIME", "EVENT_QUERY", "EXECUTE_COMMAND_LINE", "EXIT", "EXP", "EXPONENT", "EXTENDS_TYPE_OF", "FDATE", "FGET", "FGETC", "FLOOR", "FLUSH", "FNUM", "FPUT", "FPUTC", "FRACTION",
"FREE", "FSEEK", "FSTAT", "FTELL", "GAMMA", "GERROR", "GETARG", "GET_COMMAND", "GET_COMMAND_ARGUMENT", "GETCWD", "GETENV", "GET_ENVIRONMENT_VARIABLE", "GETGID", "GETLOG", "GETPID", "GETUID", "GMTIME", "HOSTNM", "HUGE", "HYPOT", "IACHAR",
"IALL", "IAND", "IANY", "IARGC", "IBCLR", "IBITS", "IBSET", "ICHAR", "IDATE", "IEOR", "IERRNO", "IMAGE_INDEX", "INDEX", "INT", "INT2", "INT8", "IOR", "IPARITY", "IRAND", "IS_IOSTAT_END", "IS_IOSTAT_EOR",
"ISATTY", "ISHFT", "ISHFTC", "ISNAN", "ITIME", "KILL", "KIND", "LBOUND", "LCOBOUND", "LEADZ", "LEN", "LEN_TRIM", "LGE", "LGT", "LINK", "LLE", "LLT", "LNBLNK", "LOC", "LOG", "LOG10",
"LOG_GAMMA", "LOGICAL", "LONG", "LSHIFT", "LSTAT", "LTIME", "MALLOC", "MASKL", "MASKR", "MATMUL", "MAX", "MAXEXPONENT", "MAXLOC", "MAXVAL", "MCLOCK", "MCLOCK8", "MERGE", "MERGE_BITS", "MIN", "MINEXPONENT", "MINLOC",
"MINVAL", "MOD", "MODULO", "MOVE_ALLOC", "MVBITS", "NEAREST", "NEW_LINE", "NINT", "NORM2", "NOT", "NULL", "NUM_IMAGES", "OR", "PACK", "PARITY", "PERROR", "POPCNT", "POPPAR", "PRECISION", "PRESENT", "PRODUCT",
"RADIX", "RAN", "RAND", "RANDOM_NUMBER", "RANDOM_SEED", "RANGE", "RANK", "REAL", "RENAME", "REPEAT", "RESHAPE", "RRSPACING", "RSHIFT", "SAME_TYPE_AS", "SCALE", "SCAN", "SECNDS", "SECOND", "SELECTED_CHAR_KIND", "SELECTED_INT_KIND", "SELECTED_REAL_KIND",
"SET_EXPONENT", "SHAPE", "SHIFTA", "SHIFTL", "SHIFTR", "SIGN", "SIGNAL", "SIN", "SINH", "SIZE", "SIZEOF", "SLEEP", "SPACING", "SPREAD", "SQRT", "SRAND", "STAT", "STORAGE_SIZE", "SUM", "SYMLNK", "SYSTEM",
"SYSTEM_CLOCK", "TAN", "TANH", "THIS_IMAGE", "TIME", "TIME8", "TINY", "TRAILZ", "TRANSFER", "TRANSPOSE", "TRIM", "TTYNAM", "UBOUND", "UCOBOUND", "UMASK", "UNLINK", "UNPACK", "VERIFY", "XOR"]

class InlineDocsHover(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if "Fortran" not in view.settings().get('syntax'):
            return
        if view.settings().get('fortran_disable_docs', False):
            return
        if hover_zone != sublime.HOVER_TEXT:
            return
        wordregion = view.word(point)
        word = view.substr(wordregion).upper()
        self.show_doc_popup(view, point, word)

    def show_doc_popup(self, view, point, word):
        if not word in intrinsics:
            return
        max_width, max_height = 600, 300
        html_str = sublime.load_resource("Packages/Fortran/minihtml/"+word+".html")
        view.show_popup(html_str,
                        sublime.HIDE_ON_MOUSE_MOVE_AWAY,
                        point,
                        max_width,
                        max_height,
                        lambda s: self.on_navigate(s, view, point),
                        )

    def on_navigate(self, href, view, point):
        # Get function name from URL
        word = href.replace("005f", "").split(".")[0]
        if word in intrinsics:
            self.show_doc_popup(view, point, word)
