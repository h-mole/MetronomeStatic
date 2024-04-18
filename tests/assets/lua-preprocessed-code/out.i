# 0 "lvm.c"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "lvm.c"
# 10 "lvm.c"
# 1 "lprefix.h" 1
# 11 "lvm.c" 2

# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/float.h" 1 3 4
# 627 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/float.h" 3 4
# 1 "C:/msys64/mingw64/include/float.h" 1 3 4
# 138 "C:/msys64/mingw64/include/float.h" 3 4
# 1 "C:/msys64/mingw64/include/crtdefs.h" 1 3 4
# 10 "C:/msys64/mingw64/include/crtdefs.h" 3 4
# 1 "C:/msys64/mingw64/include/corecrt.h" 1 3 4
# 10 "C:/msys64/mingw64/include/corecrt.h" 3 4
# 1 "C:/msys64/mingw64/include/_mingw.h" 1 3 4
# 10 "C:/msys64/mingw64/include/_mingw.h" 3 4
# 1 "C:/msys64/mingw64/include/_mingw_mac.h" 1 3 4
# 98 "C:/msys64/mingw64/include/_mingw_mac.h" 3 4
             
# 107 "C:/msys64/mingw64/include/_mingw_mac.h" 3 4
             
# 306 "C:/msys64/mingw64/include/_mingw_mac.h" 3 4
       
# 384 "C:/msys64/mingw64/include/_mingw_mac.h" 3 4
       
# 11 "C:/msys64/mingw64/include/_mingw.h" 2 3 4
# 1 "C:/msys64/mingw64/include/_mingw_secapi.h" 1 3 4
# 12 "C:/msys64/mingw64/include/_mingw.h" 2 3 4
# 282 "C:/msys64/mingw64/include/_mingw.h" 3 4
# 1 "C:/msys64/mingw64/include/vadefs.h" 1 3 4
# 9 "C:/msys64/mingw64/include/vadefs.h" 3 4
# 1 "C:/msys64/mingw64/include/_mingw.h" 1 3 4
# 661 "C:/msys64/mingw64/include/_mingw.h" 3 4
# 1 "C:/msys64/mingw64/include/sdks/_mingw_ddk.h" 1 3 4
# 662 "C:/msys64/mingw64/include/_mingw.h" 2 3 4
# 10 "C:/msys64/mingw64/include/vadefs.h" 2 3 4




#pragma pack(push,_CRT_PACKING)
# 24 "C:/msys64/mingw64/include/vadefs.h" 3 4
  
# 24 "C:/msys64/mingw64/include/vadefs.h" 3 4
 typedef __builtin_va_list __gnuc_va_list;






  typedef __gnuc_va_list va_list;
# 103 "C:/msys64/mingw64/include/vadefs.h" 3 4
#pragma pack(pop)
# 283 "C:/msys64/mingw64/include/_mingw.h" 2 3 4
# 580 "C:/msys64/mingw64/include/_mingw.h" 3 4
void __attribute__((__cdecl__)) __debugbreak(void);
extern __inline__ __attribute__((__always_inline__,__gnu_inline__)) void __attribute__((__cdecl__)) __debugbreak(void)
{

  __asm__ __volatile__("int {$}3":);







}
# 601 "C:/msys64/mingw64/include/_mingw.h" 3 4
void __attribute__((__cdecl__)) __attribute__ ((__noreturn__)) __fastfail(unsigned int code);
extern __inline__ __attribute__((__always_inline__,__gnu_inline__)) void __attribute__((__cdecl__)) __attribute__ ((__noreturn__)) __fastfail(unsigned int code)
{

  __asm__ __volatile__("int {$}0x29"::"c"(code));
# 615 "C:/msys64/mingw64/include/_mingw.h" 3 4
  __builtin_unreachable();
}
# 641 "C:/msys64/mingw64/include/_mingw.h" 3 4
const char *__mingw_get_crt_info (void);
# 11 "C:/msys64/mingw64/include/corecrt.h" 2 3 4




#pragma pack(push,_CRT_PACKING)
# 35 "C:/msys64/mingw64/include/corecrt.h" 3 4
__extension__ typedef unsigned long long size_t;
# 45 "C:/msys64/mingw64/include/corecrt.h" 3 4
__extension__ typedef long long ssize_t;






typedef size_t rsize_t;
# 62 "C:/msys64/mingw64/include/corecrt.h" 3 4
__extension__ typedef long long intptr_t;
# 75 "C:/msys64/mingw64/include/corecrt.h" 3 4
__extension__ typedef unsigned long long uintptr_t;
# 88 "C:/msys64/mingw64/include/corecrt.h" 3 4
__extension__ typedef long long ptrdiff_t;
# 98 "C:/msys64/mingw64/include/corecrt.h" 3 4
typedef unsigned short wchar_t;







typedef unsigned short wint_t;
typedef unsigned short wctype_t;





typedef int errno_t;




typedef long __time32_t;




__extension__ typedef long long __time64_t;
# 138 "C:/msys64/mingw64/include/corecrt.h" 3 4
typedef __time64_t time_t;
# 430 "C:/msys64/mingw64/include/corecrt.h" 3 4
struct threadlocaleinfostruct;
struct threadmbcinfostruct;
typedef struct threadlocaleinfostruct *pthreadlocinfo;
typedef struct threadmbcinfostruct *pthreadmbcinfo;
struct __lc_time_data;

typedef struct localeinfo_struct {
  pthreadlocinfo locinfo;
  pthreadmbcinfo mbcinfo;
} _locale_tstruct,*_locale_t;



typedef struct tagLC_ID {
  unsigned short wLanguage;
  unsigned short wCountry;
  unsigned short wCodePage;
} LC_ID,*LPLC_ID;




typedef struct threadlocaleinfostruct {





  int refcount;
  unsigned int lc_codepage;
  unsigned int lc_collate_cp;
  unsigned long lc_handle[6];
  LC_ID lc_id[6];
  struct {
    char *locale;
    wchar_t *wlocale;
    int *refcount;
    int *wrefcount;
  } lc_category[6];
  int lc_clike;
  int mb_cur_max;
  int *lconv_intl_refcount;
  int *lconv_num_refcount;
  int *lconv_mon_refcount;
  struct lconv *lconv;
  int *ctype1_refcount;
  unsigned short *ctype1;
  const unsigned short *pctype;
  const unsigned char *pclmap;
  const unsigned char *pcumap;
  struct __lc_time_data *lc_time_curr;

} threadlocinfo;
# 501 "C:/msys64/mingw64/include/corecrt.h" 3 4
#pragma pack(pop)
# 11 "C:/msys64/mingw64/include/crtdefs.h" 2 3 4
# 139 "C:/msys64/mingw64/include/float.h" 2 3 4
# 261 "C:/msys64/mingw64/include/float.h" 3 4
__attribute__ ((__dllimport__)) unsigned int __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _controlfp (unsigned int _NewValue, unsigned int _Mask) ;
__attribute__((dllimport)) errno_t __attribute__((__cdecl__)) _controlfp_s(unsigned int *_CurrentState, unsigned int _NewValue, unsigned int _Mask);
__attribute__ ((__dllimport__)) unsigned int __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _control87 (unsigned int _NewValue, unsigned int _Mask);


__attribute__ ((__dllimport__)) unsigned int __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _clearfp (void);
__attribute__ ((__dllimport__)) unsigned int __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _statusfp (void);
# 281 "C:/msys64/mingw64/include/float.h" 3 4
void __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _fpreset (void);

void __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) fpreset (void);



__attribute__ ((__dllimport__)) int * __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) __fpecode(void);
# 297 "C:/msys64/mingw64/include/float.h" 3 4
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _chgsign (double _X);
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _copysign (double _Number,double _Sign);
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _logb (double);
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _nextafter (double, double);
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _scalb (double, long);

__attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _finite (double);
__attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _fpclass (double);
__attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _isnan (double);


extern long double __attribute__((__cdecl__)) _chgsignl (long double);
# 628 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/float.h" 2 3 4
# 13 "lvm.c" 2
# 1 "C:/msys64/mingw64/include/limits.h" 1 3
# 14 "lvm.c" 2
# 1 "C:/msys64/mingw64/include/math.h" 1 3
# 10 "C:/msys64/mingw64/include/math.h" 3
       
# 11 "C:/msys64/mingw64/include/math.h" 3




struct _exception;

#pragma pack(push,_CRT_PACKING)
# 119 "C:/msys64/mingw64/include/math.h" 3
  typedef union __mingw_dbl_type_t {
    double x;
    unsigned long long val;
    __extension__ struct {
      unsigned int low, high;
    } lh;
  } __mingw_dbl_type_t;

  typedef union __mingw_flt_type_t {
    float x;
    unsigned int val;
  } __mingw_flt_type_t;

  typedef union __mingw_ldbl_type_t
  {
    long double x;
    __extension__ struct {
      unsigned int low, high;
      int sign_exponent : 16;
      int res1 : 16;
      int res0 : 32;
    } lh;
  } __mingw_ldbl_type_t;
# 150 "C:/msys64/mingw64/include/math.h" 3
  extern double * __imp__HUGE;
# 163 "C:/msys64/mingw64/include/math.h" 3
  struct _exception {
    int type;
    const char *name;
    double arg1;
    double arg2;
    double retval;
  };

  void __mingw_raise_matherr (int typ, const char *name, double a1, double a2,
         double rslt);
  void __mingw_setusermatherr (int (__attribute__((__cdecl__)) *)(struct _exception *));
  __attribute__ ((__dllimport__)) void __setusermatherr(int (__attribute__((__cdecl__)) *)(struct _exception *));



  double __attribute__((__cdecl__)) sin(double _X);
  double __attribute__((__cdecl__)) cos(double _X);
  double __attribute__((__cdecl__)) tan(double _X);
  double __attribute__((__cdecl__)) sinh(double _X);
  double __attribute__((__cdecl__)) cosh(double _X);
  double __attribute__((__cdecl__)) tanh(double _X);
  double __attribute__((__cdecl__)) asin(double _X);
  double __attribute__((__cdecl__)) acos(double _X);
  double __attribute__((__cdecl__)) atan(double _X);
  double __attribute__((__cdecl__)) atan2(double _Y,double _X);
  double __attribute__((__cdecl__)) exp(double _X);
  double __attribute__((__cdecl__)) log(double _X);
  double __attribute__((__cdecl__)) log10(double _X);
  double __attribute__((__cdecl__)) pow(double _X,double _Y);
  double __attribute__((__cdecl__)) sqrt(double _X);
  double __attribute__((__cdecl__)) ceil(double _X);
  double __attribute__((__cdecl__)) floor(double _X);


  extern float __attribute__((__cdecl__)) fabsf (float x);
  extern long double __attribute__((__cdecl__)) fabsl (long double);
  extern double __attribute__((__cdecl__)) fabs (double _X);
# 238 "C:/msys64/mingw64/include/math.h" 3
  double __attribute__((__cdecl__)) ldexp(double _X,int _Y);
  double __attribute__((__cdecl__)) frexp(double _X,int *_Y);
  double __attribute__((__cdecl__)) modf(double _X,double *_Y);
  double __attribute__((__cdecl__)) fmod(double _X,double _Y);

  void __attribute__((__cdecl__)) sincos (double __x, double *p_sin, double *p_cos);
  void __attribute__((__cdecl__)) sincosl (long double __x, long double *p_sin, long double *p_cos);
  void __attribute__((__cdecl__)) sincosf (float __x, float *p_sin, float *p_cos);



  int __attribute__((__cdecl__)) abs(int _X);
  long __attribute__((__cdecl__)) labs(long _X);



  double __attribute__((__cdecl__)) atof(const char *_String);
  double __attribute__((__cdecl__)) _atof_l(const char *_String,_locale_t _Locale);
# 265 "C:/msys64/mingw64/include/math.h" 3
  struct _complex {
    double x;
    double y;
  };


  double __attribute__((__cdecl__)) _cabs(struct _complex _ComplexA);
  double __attribute__((__cdecl__)) _hypot(double _X,double _Y);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _j0(double _X);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _j1(double _X);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _jn(int _X,double _Y);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _y0(double _X);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _y1(double _X);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _yn(int _X,double _Y);


  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _matherr (struct _exception *);
# 306 "C:/msys64/mingw64/include/math.h" 3
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) j0 (double) ;
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) j1 (double) ;
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) jn (int, double) ;
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) y0 (double) ;
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) y1 (double) ;
__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) yn (int, double) ;

__attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) chgsign (double);
# 322 "C:/msys64/mingw64/include/math.h" 3
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) finite (double);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) fpclass (double);
# 367 "C:/msys64/mingw64/include/math.h" 3
typedef float float_t;
typedef double double_t;
# 402 "C:/msys64/mingw64/include/math.h" 3
  extern int __attribute__((__cdecl__)) __fpclassifyl (long double);
  extern int __attribute__((__cdecl__)) __fpclassifyf (float);
  extern int __attribute__((__cdecl__)) __fpclassify (double);
# 515 "C:/msys64/mingw64/include/math.h" 3
  extern int __attribute__((__cdecl__)) __isnan (double);
  extern int __attribute__((__cdecl__)) __isnanf (float);
  extern int __attribute__((__cdecl__)) __isnanl (long double);
# 602 "C:/msys64/mingw64/include/math.h" 3
  extern int __attribute__((__cdecl__)) __signbit (double);
  extern int __attribute__((__cdecl__)) __signbitf (float);
  extern int __attribute__((__cdecl__)) __signbitl (long double);
# 659 "C:/msys64/mingw64/include/math.h" 3
  extern float __attribute__((__cdecl__)) sinf(float _X);
  extern long double __attribute__((__cdecl__)) sinl(long double);

  extern float __attribute__((__cdecl__)) cosf(float _X);
  extern long double __attribute__((__cdecl__)) cosl(long double);

  extern float __attribute__((__cdecl__)) tanf(float _X);
  extern long double __attribute__((__cdecl__)) tanl(long double);
  extern float __attribute__((__cdecl__)) asinf(float _X);
  extern long double __attribute__((__cdecl__)) asinl(long double);

  extern float __attribute__((__cdecl__)) acosf (float);
  extern long double __attribute__((__cdecl__)) acosl (long double);

  extern float __attribute__((__cdecl__)) atanf (float);
  extern long double __attribute__((__cdecl__)) atanl (long double);

  extern float __attribute__((__cdecl__)) atan2f (float, float);
  extern long double __attribute__((__cdecl__)) atan2l (long double, long double);


  extern float __attribute__((__cdecl__)) sinhf(float _X);



  extern long double __attribute__((__cdecl__)) sinhl(long double);

  extern float __attribute__((__cdecl__)) coshf(float _X);



  extern long double __attribute__((__cdecl__)) coshl(long double);

  extern float __attribute__((__cdecl__)) tanhf(float _X);



  extern long double __attribute__((__cdecl__)) tanhl(long double);



  extern double __attribute__((__cdecl__)) acosh (double);
  extern float __attribute__((__cdecl__)) acoshf (float);
  extern long double __attribute__((__cdecl__)) acoshl (long double);


  extern double __attribute__((__cdecl__)) asinh (double);
  extern float __attribute__((__cdecl__)) asinhf (float);
  extern long double __attribute__((__cdecl__)) asinhl (long double);


  extern double __attribute__((__cdecl__)) atanh (double);
  extern float __attribute__((__cdecl__)) atanhf (float);
  extern long double __attribute__((__cdecl__)) atanhl (long double);



  extern float __attribute__((__cdecl__)) expf(float _X);



  extern long double __attribute__((__cdecl__)) expl(long double);


  extern double __attribute__((__cdecl__)) exp2(double);
  extern float __attribute__((__cdecl__)) exp2f(float);
  extern long double __attribute__((__cdecl__)) exp2l(long double);



  extern double __attribute__((__cdecl__)) expm1(double);
  extern float __attribute__((__cdecl__)) expm1f(float);
  extern long double __attribute__((__cdecl__)) expm1l(long double);


  extern float frexpf(float _X,int *_Y);



  extern long double __attribute__((__cdecl__)) frexpl(long double,int *);




  extern int __attribute__((__cdecl__)) ilogb (double);
  extern int __attribute__((__cdecl__)) ilogbf (float);
  extern int __attribute__((__cdecl__)) ilogbl (long double);


  extern float __attribute__((__cdecl__)) ldexpf(float _X,int _Y);



  extern long double __attribute__((__cdecl__)) ldexpl (long double, int);


  extern float __attribute__((__cdecl__)) logf (float);
  extern long double __attribute__((__cdecl__)) logl(long double);


  extern float __attribute__((__cdecl__)) log10f (float);
  extern long double __attribute__((__cdecl__)) log10l(long double);


  extern double __attribute__((__cdecl__)) log1p(double);
  extern float __attribute__((__cdecl__)) log1pf(float);
  extern long double __attribute__((__cdecl__)) log1pl(long double);


  extern double __attribute__((__cdecl__)) log2 (double);
  extern float __attribute__((__cdecl__)) log2f (float);
  extern long double __attribute__((__cdecl__)) log2l (long double);


  extern double __attribute__((__cdecl__)) logb (double);
  extern float __attribute__((__cdecl__)) logbf (float);
  extern long double __attribute__((__cdecl__)) logbl (long double);
# 862 "C:/msys64/mingw64/include/math.h" 3
  extern float __attribute__((__cdecl__)) modff (float, float*);
  extern long double __attribute__((__cdecl__)) modfl (long double, long double*);


  extern double __attribute__((__cdecl__)) scalbn (double, int);
  extern float __attribute__((__cdecl__)) scalbnf (float, int);
  extern long double __attribute__((__cdecl__)) scalbnl (long double, int);

  extern double __attribute__((__cdecl__)) scalbln (double, long);
  extern float __attribute__((__cdecl__)) scalblnf (float, long);
  extern long double __attribute__((__cdecl__)) scalblnl (long double, long);



  extern double __attribute__((__cdecl__)) cbrt (double);
  extern float __attribute__((__cdecl__)) cbrtf (float);
  extern long double __attribute__((__cdecl__)) cbrtl (long double);


  extern double __attribute__((__cdecl__)) hypot (double, double) ;
  extern float __attribute__((__cdecl__)) hypotf (float x, float y);



  extern long double __attribute__((__cdecl__)) hypotl (long double, long double);


  extern float __attribute__((__cdecl__)) powf(float _X,float _Y);



  extern long double __attribute__((__cdecl__)) powl (long double, long double);


  extern float __attribute__((__cdecl__)) sqrtf (float);
  extern long double sqrtl(long double);


  extern double __attribute__((__cdecl__)) erf (double);
  extern float __attribute__((__cdecl__)) erff (float);
  extern long double __attribute__((__cdecl__)) erfl (long double);


  extern double __attribute__((__cdecl__)) erfc (double);
  extern float __attribute__((__cdecl__)) erfcf (float);
  extern long double __attribute__((__cdecl__)) erfcl (long double);


  extern double __attribute__((__cdecl__)) lgamma (double);
  extern float __attribute__((__cdecl__)) lgammaf (float);
  extern long double __attribute__((__cdecl__)) lgammal (long double);

  extern int signgam;


  extern double __attribute__((__cdecl__)) tgamma (double);
  extern float __attribute__((__cdecl__)) tgammaf (float);
  extern long double __attribute__((__cdecl__)) tgammal (long double);


  extern float __attribute__((__cdecl__)) ceilf (float);
  extern long double __attribute__((__cdecl__)) ceill (long double);


  extern float __attribute__((__cdecl__)) floorf (float);
  extern long double __attribute__((__cdecl__)) floorl (long double);


  extern double __attribute__((__cdecl__)) nearbyint ( double);
  extern float __attribute__((__cdecl__)) nearbyintf (float);
  extern long double __attribute__((__cdecl__)) nearbyintl (long double);



extern double __attribute__((__cdecl__)) rint (double);
extern float __attribute__((__cdecl__)) rintf (float);
extern long double __attribute__((__cdecl__)) rintl (long double);


extern long __attribute__((__cdecl__)) lrint (double);
extern long __attribute__((__cdecl__)) lrintf (float);
extern long __attribute__((__cdecl__)) lrintl (long double);

__extension__ long long __attribute__((__cdecl__)) llrint (double);
__extension__ long long __attribute__((__cdecl__)) llrintf (float);
__extension__ long long __attribute__((__cdecl__)) llrintl (long double);
# 1029 "C:/msys64/mingw64/include/math.h" 3
  extern double __attribute__((__cdecl__)) round (double);
  extern float __attribute__((__cdecl__)) roundf (float);
  extern long double __attribute__((__cdecl__)) roundl (long double);


  extern long __attribute__((__cdecl__)) lround (double);
  extern long __attribute__((__cdecl__)) lroundf (float);
  extern long __attribute__((__cdecl__)) lroundl (long double);
  __extension__ long long __attribute__((__cdecl__)) llround (double);
  __extension__ long long __attribute__((__cdecl__)) llroundf (float);
  __extension__ long long __attribute__((__cdecl__)) llroundl (long double);



  extern double __attribute__((__cdecl__)) trunc (double);
  extern float __attribute__((__cdecl__)) truncf (float);
  extern long double __attribute__((__cdecl__)) truncl (long double);


  extern float __attribute__((__cdecl__)) fmodf (float, float);
  extern long double __attribute__((__cdecl__)) fmodl (long double, long double);


  extern double __attribute__((__cdecl__)) remainder (double, double);
  extern float __attribute__((__cdecl__)) remainderf (float, float);
  extern long double __attribute__((__cdecl__)) remainderl (long double, long double);


  extern double __attribute__((__cdecl__)) remquo(double, double, int *);
  extern float __attribute__((__cdecl__)) remquof(float, float, int *);
  extern long double __attribute__((__cdecl__)) remquol(long double, long double, int *);


  extern double __attribute__((__cdecl__)) copysign (double, double);
  extern float __attribute__((__cdecl__)) copysignf (float, float);
  extern long double __attribute__((__cdecl__)) copysignl (long double, long double);
# 1086 "C:/msys64/mingw64/include/math.h" 3
  extern double __attribute__((__cdecl__)) nan(const char *tagp);
  extern float __attribute__((__cdecl__)) nanf(const char *tagp);
  extern long double __attribute__((__cdecl__)) nanl(const char *tagp);
# 1097 "C:/msys64/mingw64/include/math.h" 3
  extern double __attribute__((__cdecl__)) nextafter (double, double);
  extern float __attribute__((__cdecl__)) nextafterf (float, float);
  extern long double __attribute__((__cdecl__)) nextafterl (long double, long double);


  extern double __attribute__((__cdecl__)) nexttoward (double, long double);
  extern float __attribute__((__cdecl__)) nexttowardf (float, long double);
  extern long double __attribute__((__cdecl__)) nexttowardl (long double, long double);



  extern double __attribute__((__cdecl__)) fdim (double x, double y);
  extern float __attribute__((__cdecl__)) fdimf (float x, float y);
  extern long double __attribute__((__cdecl__)) fdiml (long double x, long double y);







  extern double __attribute__((__cdecl__)) fmax (double, double);
  extern float __attribute__((__cdecl__)) fmaxf (float, float);
  extern long double __attribute__((__cdecl__)) fmaxl (long double, long double);


  extern double __attribute__((__cdecl__)) fmin (double, double);
  extern float __attribute__((__cdecl__)) fminf (float, float);
  extern long double __attribute__((__cdecl__)) fminl (long double, long double);



  extern double __attribute__((__cdecl__)) fma (double, double, double);
  extern float __attribute__((__cdecl__)) fmaf (float, float, float);
  extern long double __attribute__((__cdecl__)) fmal (long double, long double, long double);
# 1180 "C:/msys64/mingw64/include/math.h" 3
   __attribute__ ((__dllimport__)) float __attribute__((__cdecl__)) _copysignf (float _Number,float _Sign);
   __attribute__ ((__dllimport__)) float __attribute__((__cdecl__)) _chgsignf (float _X);
   __attribute__ ((__dllimport__)) float __attribute__((__cdecl__)) _logbf(float _X);
   __attribute__ ((__dllimport__)) float __attribute__((__cdecl__)) _nextafterf(float _X,float _Y);
   __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _finitef(float _X);
   __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _isnanf(float _X);
   __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fpclassf(float _X);



   extern long double __attribute__((__cdecl__)) _chgsignl (long double);
# 1580 "C:/msys64/mingw64/include/math.h" 3
#pragma pack(pop)
# 15 "lvm.c" 2
# 1 "C:/msys64/mingw64/include/stdio.h" 1 3
# 9 "C:/msys64/mingw64/include/stdio.h" 3
# 1 "C:/msys64/mingw64/include/corecrt_stdio_config.h" 1 3
# 10 "C:/msys64/mingw64/include/stdio.h" 2 3

#pragma pack(push,_CRT_PACKING)

       

       

       

       
# 33 "C:/msys64/mingw64/include/stdio.h" 3
  struct _iobuf {



    char *_ptr;
    int _cnt;
    char *_base;
    int _flag;
    int _file;
    int _charbuf;
    int _bufsiz;
    char *_tmpfname;

  };
  typedef struct _iobuf FILE;
# 91 "C:/msys64/mingw64/include/stdio.h" 3
# 1 "C:/msys64/mingw64/include/_mingw_off_t.h" 1 3




  typedef long _off_t;

  typedef long off32_t;





  __extension__ typedef long long _off64_t;

  __extension__ typedef long long off64_t;
# 24 "C:/msys64/mingw64/include/_mingw_off_t.h" 3
typedef off64_t off_t;
# 92 "C:/msys64/mingw64/include/stdio.h" 2 3

__attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) __acrt_iob_func(unsigned index);


  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) __iob_func(void);
# 115 "C:/msys64/mingw64/include/stdio.h" 3
  __extension__ typedef long long fpos_t;
# 156 "C:/msys64/mingw64/include/stdio.h" 3
extern
  __attribute__((__format__ (gnu_scanf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_sscanf(const char * __restrict__ _Src,const char * __restrict__ _Format,...);
extern
  __attribute__((__format__ (gnu_scanf, 2, 0))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vsscanf (const char * __restrict__ _Str,const char * __restrict__ Format,va_list argp);
extern
  __attribute__((__format__ (gnu_scanf, 1, 2))) __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_scanf(const char * __restrict__ _Format,...);
extern
  __attribute__((__format__ (gnu_scanf, 1, 0))) __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_vscanf(const char * __restrict__ Format, va_list argp);
extern
  __attribute__((__format__ (gnu_scanf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_fscanf(FILE * __restrict__ _File,const char * __restrict__ _Format,...);
extern
  __attribute__((__format__ (gnu_scanf, 2, 0))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vfscanf (FILE * __restrict__ fp, const char * __restrict__ Format,va_list argp);

extern
  __attribute__((__format__ (gnu_printf, 3, 0))) __attribute__ ((__nonnull__ (3)))
  int __attribute__((__cdecl__)) __mingw_vsnprintf(char * __restrict__ _DstBuf,size_t _MaxCount,const char * __restrict__ _Format,
                               va_list _ArgList);
extern
  __attribute__((__format__ (gnu_printf, 3, 4))) __attribute__ ((__nonnull__ (3)))
  int __attribute__((__cdecl__)) __mingw_snprintf(char * __restrict__ s, size_t n, const char * __restrict__ format, ...);
extern
  __attribute__((__format__ (gnu_printf, 1, 2))) __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_printf(const char * __restrict__ , ... ) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (gnu_printf, 1, 0))) __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_vprintf (const char * __restrict__ , va_list) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (gnu_printf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_fprintf (FILE * __restrict__ , const char * __restrict__ , ...) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (gnu_printf, 2, 0))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vfprintf (FILE * __restrict__ , const char * __restrict__ , va_list) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (gnu_printf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_sprintf (char * __restrict__ , const char * __restrict__ , ...) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (gnu_printf, 2, 0))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vsprintf (char * __restrict__ , const char * __restrict__ , va_list) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (gnu_printf, 2, 3))) __attribute__((nonnull (1,2)))
  int __attribute__((__cdecl__)) __mingw_asprintf(char ** __restrict__ , const char * __restrict__ , ...) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (gnu_printf, 2, 0))) __attribute__((nonnull (1,2)))
  int __attribute__((__cdecl__)) __mingw_vasprintf(char ** __restrict__ , const char * __restrict__ , va_list) __attribute__ ((__nothrow__));

extern
  __attribute__((__format__ (ms_scanf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_sscanf(const char * __restrict__ _Src,const char * __restrict__ _Format,...);
extern
  __attribute__((__format__ (ms_scanf, 1, 2))) __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __ms_scanf(const char * __restrict__ _Format,...);
extern
  __attribute__((__format__ (ms_scanf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_fscanf(FILE * __restrict__ _File,const char * __restrict__ _Format,...);

extern
  __attribute__((__format__ (ms_printf, 1, 2))) __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __ms_printf(const char * __restrict__ , ... ) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (ms_printf, 1, 0))) __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __ms_vprintf (const char * __restrict__ , va_list) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (ms_printf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_fprintf (FILE * __restrict__ , const char * __restrict__ , ...) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (ms_printf, 2, 0))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_vfprintf (FILE * __restrict__ , const char * __restrict__ , va_list) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (ms_printf, 2, 3))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_sprintf (char * __restrict__ , const char * __restrict__ , ...) __attribute__ ((__nothrow__));
extern
  __attribute__((__format__ (ms_printf, 2, 0))) __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_vsprintf (char * __restrict__ , const char * __restrict__ , va_list) __attribute__ ((__nothrow__));
# 288 "C:/msys64/mingw64/include/stdio.h" 3
static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_scanf, 2, 3))) __attribute__ ((__nonnull__ (2)))
int sscanf(const char *__source, const char *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vsscanf( __source, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_scanf, 1, 2))) __attribute__ ((__nonnull__ (1)))
int scanf(const char *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfscanf( (__acrt_iob_func(0)), __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_scanf, 2, 3))) __attribute__ ((__nonnull__ (2)))
int fscanf(FILE *__stream, const char *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfscanf( __stream, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}



#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wshadow"


static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_scanf, 2, 0))) __attribute__ ((__nonnull__ (2)))
int vsscanf (const char *__source, const char *__format, __builtin_va_list __local_argv)
{
  return __mingw_vsscanf( __source, __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_scanf, 1, 0))) __attribute__ ((__nonnull__ (1)))
int vscanf(const char *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfscanf( (__acrt_iob_func(0)), __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_scanf, 2, 0))) __attribute__ ((__nonnull__ (2)))
int vfscanf (FILE *__stream, const char *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfscanf( __stream, __format, __local_argv );
}


#pragma GCC diagnostic pop





static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 2, 3))) __attribute__ ((__nonnull__ (2)))
int fprintf (FILE *__stream, const char *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfprintf( __stream, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 1, 2))) __attribute__ ((__nonnull__ (1)))
int printf (const char *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfprintf( (__acrt_iob_func(1)), __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}
# 396 "C:/msys64/mingw64/include/stdio.h" 3
static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 2, 3))) __attribute__ ((__nonnull__ (2)))
int sprintf (char *__stream, const char *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vsprintf( __stream, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}



static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 2, 0))) __attribute__ ((__nonnull__ (2)))
int vfprintf (FILE *__stream, const char *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfprintf( __stream, __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 1, 0))) __attribute__ ((__nonnull__ (1)))
int vprintf (const char *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfprintf( (__acrt_iob_func(1)), __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 2, 0))) __attribute__ ((__nonnull__ (2)))
int vsprintf (char *__stream, const char *__format, __builtin_va_list __local_argv)
{
# 435 "C:/msys64/mingw64/include/stdio.h" 3
  return __mingw_vsprintf( __stream, __format, __local_argv );
}
# 453 "C:/msys64/mingw64/include/stdio.h" 3
static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 3, 4))) __attribute__ ((__nonnull__ (3)))
int snprintf (char *__stream, size_t __n, const char *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vsnprintf( __stream, __n, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}



static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
__attribute__((__format__ (gnu_printf, 3, 0))) __attribute__ ((__nonnull__ (3)))
int vsnprintf (char *__stream, size_t __n, const char *__format, __builtin_va_list __local_argv)
{



  return __mingw_vsnprintf( __stream, __n, __format, __local_argv );
}
# 607 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _filbuf(FILE *_File);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _flsbuf(int _Ch,FILE *_File);



  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _fsopen(const char *_Filename,const char *_Mode,int _ShFlag);

  void __attribute__((__cdecl__)) clearerr(FILE *_File);
  int __attribute__((__cdecl__)) fclose(FILE *_File);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fcloseall(void);



  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _fdopen(int _FileHandle,const char *_Mode);

  int __attribute__((__cdecl__)) feof(FILE *_File);
  int __attribute__((__cdecl__)) ferror(FILE *_File);
  int __attribute__((__cdecl__)) fflush(FILE *_File);
  int __attribute__((__cdecl__)) fgetc(FILE *_File);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fgetchar(void);
  int __attribute__((__cdecl__)) fgetpos(FILE * __restrict__ _File ,fpos_t * __restrict__ _Pos);
  int __attribute__((__cdecl__)) fgetpos64(FILE * __restrict__ _File ,fpos_t * __restrict__ _Pos);
  char *__attribute__((__cdecl__)) fgets(char * __restrict__ _Buf,int _MaxCount,FILE * __restrict__ _File);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fileno(FILE *_File);



  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _tempnam(const char *_DirName,const char *_FilePrefix);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _flushall(void);
  FILE *__attribute__((__cdecl__)) fopen(const char * __restrict__ _Filename,const char * __restrict__ _Mode) ;
  FILE *fopen64(const char * __restrict__ filename,const char * __restrict__ mode);
  int __attribute__((__cdecl__)) fputc(int _Ch,FILE *_File);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fputchar(int _Ch);
  int __attribute__((__cdecl__)) fputs(const char * __restrict__ _Str,FILE * __restrict__ _File);
  size_t __attribute__((__cdecl__)) fread(void * __restrict__ _DstBuf,size_t _ElementSize,size_t _Count,FILE * __restrict__ _File);
  FILE *__attribute__((__cdecl__)) freopen(const char * __restrict__ _Filename,const char * __restrict__ _Mode,FILE * __restrict__ _File) ;
  int __attribute__((__cdecl__)) fsetpos(FILE *_File,const fpos_t *_Pos);
  int __attribute__((__cdecl__)) fsetpos64(FILE *_File,const fpos_t *_Pos);
  int __attribute__((__cdecl__)) fseek(FILE *_File,long _Offset,int _Origin);
  long __attribute__((__cdecl__)) ftell(FILE *_File);



  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fseeki64(FILE *_File,long long _Offset,int _Origin);
  __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _ftelli64(FILE *_File);
# 666 "C:/msys64/mingw64/include/stdio.h" 3
  int fseeko64(FILE* stream, _off64_t offset, int whence);
  int fseeko(FILE* stream, _off_t offset, int whence);

  _off_t ftello(FILE * stream);
  _off64_t ftello64(FILE * stream);
# 687 "C:/msys64/mingw64/include/stdio.h" 3
  size_t __attribute__((__cdecl__)) fwrite(const void * __restrict__ _Str,size_t _Size,size_t _Count,FILE * __restrict__ _File);
  int __attribute__((__cdecl__)) getc(FILE *_File);
  int __attribute__((__cdecl__)) getchar(void);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _getmaxstdio(void);
  char *__attribute__((__cdecl__)) gets(char *_Buffer)
    __attribute__((__warning__("Using gets() is always unsafe - use fgets() instead")));
  int __attribute__((__cdecl__)) _getw(FILE *_File);


  void __attribute__((__cdecl__)) perror(const char *_ErrMsg);


  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _pclose(FILE *_File);
  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _popen(const char *_Command,const char *_Mode);





  int __attribute__((__cdecl__)) putc(int _Ch,FILE *_File);
  int __attribute__((__cdecl__)) putchar(int _Ch);
  int __attribute__((__cdecl__)) puts(const char *_Str);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _putw(int _Word,FILE *_File);


  int __attribute__((__cdecl__)) remove(const char *_Filename);
  int __attribute__((__cdecl__)) rename(const char *_OldFilename,const char *_NewFilename);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _unlink(const char *_Filename);

  int __attribute__((__cdecl__)) unlink(const char *_Filename) ;


  void __attribute__((__cdecl__)) rewind(FILE *_File);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _rmtmp(void);
  void __attribute__((__cdecl__)) setbuf(FILE * __restrict__ _File,char * __restrict__ _Buffer) ;
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _setmaxstdio(int _Max);
  __attribute__ ((__dllimport__)) unsigned int __attribute__((__cdecl__)) _set_output_format(unsigned int _Format);
  __attribute__ ((__dllimport__)) unsigned int __attribute__((__cdecl__)) _get_output_format(void);
  int __attribute__((__cdecl__)) setvbuf(FILE * __restrict__ _File,char * __restrict__ _Buf,int _Mode,size_t _Size);
# 751 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__pure__))
  __attribute__((__format__ (ms_printf, 1, 2))) __attribute__ ((__nonnull__ (1)))
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scprintf(const char * __restrict__ _Format,...);
  __attribute__((__format__ (ms_scanf, 3, 4))) __attribute__ ((__nonnull__ (3)))
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snscanf(const char * __restrict__ _Src,size_t _MaxCount,const char * __restrict__ _Format,...) ;

  __attribute__ ((__pure__))
  __attribute__((__format__ (ms_printf, 1, 0))) __attribute__ ((__nonnull__ (1)))
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vscprintf(const char * __restrict__ _Format,va_list _ArgList);
  FILE *__attribute__((__cdecl__)) tmpfile(void) ;
  char *__attribute__((__cdecl__)) tmpnam(char *_Buffer);
  int __attribute__((__cdecl__)) ungetc(int _Ch,FILE *_File);
# 779 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__((__format__ (ms_printf, 3, 4))) __attribute__ ((__nonnull__ (3)))
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snprintf(char * __restrict__ _Dest,size_t _Count,const char * __restrict__ _Format,...) ;
  __attribute__((__format__ (ms_printf, 3, 0))) __attribute__ ((__nonnull__ (3)))
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnprintf(char * __restrict__ _Dest,size_t _Count,const char * __restrict__ _Format,va_list _Args) ;
# 1004 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _set_printf_count_output(int _Value);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _get_printf_count_output(void);




                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_swscanf(const wchar_t * __restrict__ _Src,const wchar_t * __restrict__ _Format,...);
                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vswscanf (const wchar_t * __restrict__ _Str,const wchar_t * __restrict__ Format,va_list argp);
                                                     __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_wscanf(const wchar_t * __restrict__ _Format,...);
                                                     __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_vwscanf(const wchar_t * __restrict__ Format, va_list argp);
                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_fwscanf(FILE * __restrict__ _File,const wchar_t * __restrict__ _Format,...);
                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vfwscanf (FILE * __restrict__ fp, const wchar_t * __restrict__ Format,va_list argp);

                                                      __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_fwprintf(FILE * __restrict__ _File,const wchar_t * __restrict__ _Format,...);
                                                      __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_wprintf(const wchar_t * __restrict__ _Format,...);
                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vfwprintf(FILE * __restrict__ _File,const wchar_t * __restrict__ _Format,va_list _ArgList);
                                                     __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __mingw_vwprintf(const wchar_t * __restrict__ _Format,va_list _ArgList);
                                                      __attribute__ ((__nonnull__ (3)))
  int __attribute__((__cdecl__)) __mingw_snwprintf (wchar_t * __restrict__ s, size_t n, const wchar_t * __restrict__ format, ...);
                                                      __attribute__ ((__nonnull__ (3)))
  int __attribute__((__cdecl__)) __mingw_vsnwprintf (wchar_t * __restrict__ , size_t, const wchar_t * __restrict__ , va_list);
                                                      __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_swprintf(wchar_t * __restrict__ , const wchar_t * __restrict__ , ...);
                                                      __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __mingw_vswprintf(wchar_t * __restrict__ , const wchar_t * __restrict__ ,va_list);

                                                    __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_swscanf(const wchar_t * __restrict__ _Src,const wchar_t * __restrict__ _Format,...);
                                                    __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __ms_wscanf(const wchar_t * __restrict__ _Format,...);
                                                    __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_fwscanf(FILE * __restrict__ _File,const wchar_t * __restrict__ _Format,...);

                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_fwprintf(FILE * __restrict__ _File,const wchar_t * __restrict__ _Format,...);
                                                     __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __ms_wprintf(const wchar_t * __restrict__ _Format,...);
                                                    __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_vfwprintf(FILE * __restrict__ _File,const wchar_t * __restrict__ _Format,va_list _ArgList);
                                                    __attribute__ ((__nonnull__ (1)))
  int __attribute__((__cdecl__)) __ms_vwprintf(const wchar_t * __restrict__ _Format,va_list _ArgList);
                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_swprintf(wchar_t * __restrict__ , const wchar_t * __restrict__ , ...);
                                                     __attribute__ ((__nonnull__ (2)))
  int __attribute__((__cdecl__)) __ms_vswprintf(wchar_t * __restrict__ , const wchar_t * __restrict__ ,va_list);
# 1072 "C:/msys64/mingw64/include/stdio.h" 3
static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                     __attribute__ ((__nonnull__ (2)))
int swscanf(const wchar_t *__source, const wchar_t *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vswscanf( __source, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                     __attribute__ ((__nonnull__ (1)))
int wscanf(const wchar_t *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfwscanf( (__acrt_iob_func(0)), __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                     __attribute__ ((__nonnull__ (2)))
int fwscanf(FILE *__stream, const wchar_t *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfwscanf( __stream, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}


static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                     __attribute__ ((__nonnull__ (2)))
int vswscanf (const wchar_t * __restrict__ __source, const wchar_t * __restrict__ __format, __builtin_va_list __local_argv)
{
  return __mingw_vswscanf( __source, __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                     __attribute__ ((__nonnull__ (1)))
int vwscanf(const wchar_t *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfwscanf( (__acrt_iob_func(0)), __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                     __attribute__ ((__nonnull__ (2)))
int vfwscanf (FILE *__stream, const wchar_t *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfwscanf( __stream, __format, __local_argv );
}




static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (2)))
int fwprintf (FILE *__stream, const wchar_t *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfwprintf( __stream, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (1)))
int wprintf (const wchar_t *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vfwprintf( (__acrt_iob_func(1)), __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (2)))
int vfwprintf (FILE *__stream, const wchar_t *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfwprintf( __stream, __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (1)))
int vwprintf (const wchar_t *__format, __builtin_va_list __local_argv)
{
  return __mingw_vfwprintf( (__acrt_iob_func(1)), __format, __local_argv );
}
# 1182 "C:/msys64/mingw64/include/stdio.h" 3
static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (3)))
int snwprintf (wchar_t *__stream, size_t __n, const wchar_t *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv; __builtin_va_start( __local_argv, __format );
  __retval = __mingw_vsnwprintf( __stream, __n, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}



static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (3)))
int vsnwprintf (wchar_t *__stream, size_t __n, const wchar_t *__format, __builtin_va_list __local_argv)
{



  return __mingw_vsnwprintf( __stream, __n, __format, __local_argv );
}
# 1335 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _wfsopen(const wchar_t *_Filename,const wchar_t *_Mode,int _ShFlag);


  wint_t __attribute__((__cdecl__)) fgetwc(FILE *_File);
  __attribute__ ((__dllimport__)) wint_t __attribute__((__cdecl__)) _fgetwchar(void);
  wint_t __attribute__((__cdecl__)) fputwc(wchar_t _Ch,FILE *_File);
  __attribute__ ((__dllimport__)) wint_t __attribute__((__cdecl__)) _fputwchar(wchar_t _Ch);
  wint_t __attribute__((__cdecl__)) getwc(FILE *_File);
  wint_t __attribute__((__cdecl__)) getwchar(void);
  wint_t __attribute__((__cdecl__)) putwc(wchar_t _Ch,FILE *_File);
  wint_t __attribute__((__cdecl__)) putwchar(wchar_t _Ch);
  wint_t __attribute__((__cdecl__)) ungetwc(wint_t _Ch,FILE *_File);
  wchar_t *__attribute__((__cdecl__)) fgetws(wchar_t * __restrict__ _Dst,int _SizeInWords,FILE * __restrict__ _File);
  int __attribute__((__cdecl__)) fputws(const wchar_t * __restrict__ _Str,FILE * __restrict__ _File);
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _getws(wchar_t *_String) ;
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _putws(const wchar_t *_Str);
# 1417 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scwprintf(const wchar_t * __restrict__ _Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swprintf_c(wchar_t * __restrict__ _DstBuf,size_t _SizeInWords,const wchar_t * __restrict__ _Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vswprintf_c(wchar_t * __restrict__ _DstBuf,size_t _SizeInWords,const wchar_t * __restrict__ _Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwprintf(wchar_t * __restrict__ _Dest,size_t _Count,const wchar_t * __restrict__ _Format,...) ;
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnwprintf(wchar_t * __restrict__ _Dest,size_t _Count,const wchar_t * __restrict__ _Format,va_list _Args) ;
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vscwprintf(const wchar_t * __restrict__ _Format,va_list _ArgList);
# 1447 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swprintf(wchar_t * __restrict__ _Dest,const wchar_t * __restrict__ _Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vswprintf(wchar_t * __restrict__ _Dest,const wchar_t * __restrict__ _Format,va_list _Args);



# 1 "C:/msys64/mingw64/include/swprintf.inl" 1 3
# 25 "C:/msys64/mingw64/include/swprintf.inl" 3
static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (3)))
int vswprintf (wchar_t *__stream, size_t __count, const wchar_t *__format, __builtin_va_list __local_argv)
{
  return vsnwprintf( __stream, __count, __format, __local_argv );
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
                                                      __attribute__ ((__nonnull__ (3)))
int swprintf (wchar_t *__stream, size_t __count, const wchar_t *__format, ...)
{
  int __retval;
  __builtin_va_list __local_argv;

  __builtin_va_start( __local_argv, __format );
  __retval = vswprintf( __stream, __count, __format, __local_argv );
  __builtin_va_end( __local_argv );
  return __retval;
}
# 1453 "C:/msys64/mingw64/include/stdio.h" 2 3
# 1462 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wtempnam(const wchar_t *_Directory,const wchar_t *_FilePrefix);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwscanf(const wchar_t * __restrict__ _Src,size_t _MaxCount,const wchar_t * __restrict__ _Format,...);
  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _wfdopen(int _FileHandle ,const wchar_t *_Mode);
  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _wfopen(const wchar_t * __restrict__ _Filename,const wchar_t *__restrict__ _Mode) ;
  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _wfreopen(const wchar_t * __restrict__ _Filename,const wchar_t * __restrict__ _Mode,FILE * __restrict__ _OldFile) ;



  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _wperror(const wchar_t *_ErrMsg);

  __attribute__ ((__dllimport__)) FILE *__attribute__((__cdecl__)) _wpopen(const wchar_t *_Command,const wchar_t *_Mode);




  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wremove(const wchar_t *_Filename);
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wtmpnam(wchar_t *_Buffer);
# 1522 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _lock_file(FILE *_File);
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _unlock_file(FILE *_File);
# 1540 "C:/msys64/mingw64/include/stdio.h" 3
  char *__attribute__((__cdecl__)) tempnam(const char *_Directory,const char *_FilePrefix) ;
  int __attribute__((__cdecl__)) fcloseall(void) ;
  FILE *__attribute__((__cdecl__)) fdopen(int _FileHandle,const char *_Format) ;
  int __attribute__((__cdecl__)) fgetchar(void) ;
  int __attribute__((__cdecl__)) fileno(FILE *_File) ;
  int __attribute__((__cdecl__)) flushall(void) ;
  int __attribute__((__cdecl__)) fputchar(int _Ch) ;
  int __attribute__((__cdecl__)) getw(FILE *_File) ;
  int __attribute__((__cdecl__)) putw(int _Ch,FILE *_File) ;
  int __attribute__((__cdecl__)) rmtmp(void) ;
# 1566 "C:/msys64/mingw64/include/stdio.h" 3
int __attribute__((__cdecl__)) __mingw_str_wide_utf8 (const wchar_t * const wptr, char **mbptr, size_t * buflen);
# 1580 "C:/msys64/mingw64/include/stdio.h" 3
int __attribute__((__cdecl__)) __mingw_str_utf8_wide (const char *const mbptr, wchar_t ** wptr, size_t * buflen);
# 1589 "C:/msys64/mingw64/include/stdio.h" 3
void __attribute__((__cdecl__)) __mingw_str_free(void *ptr);






  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnl(int _Mode,const wchar_t *_Filename,const wchar_t *_ArgList,...);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnle(int _Mode,const wchar_t *_Filename,const wchar_t *_ArgList,...);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnlp(int _Mode,const wchar_t *_Filename,const wchar_t *_ArgList,...);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnlpe(int _Mode,const wchar_t *_Filename,const wchar_t *_ArgList,...);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnv(int _Mode,const wchar_t *_Filename,const wchar_t *const *_ArgList);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnve(int _Mode,const wchar_t *_Filename,const wchar_t *const *_ArgList,const wchar_t *const *_Env);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnvp(int _Mode,const wchar_t *_Filename,const wchar_t *const *_ArgList);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _wspawnvpe(int _Mode,const wchar_t *_Filename,const wchar_t *const *_ArgList,const wchar_t *const *_Env);
# 1620 "C:/msys64/mingw64/include/stdio.h" 3
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _spawnv(int _Mode,const char *_Filename,const char *const *_ArgList);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _spawnve(int _Mode,const char *_Filename,const char *const *_ArgList,const char *const *_Env);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _spawnvp(int _Mode,const char *_Filename,const char *const *_ArgList);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _spawnvpe(int _Mode,const char *_Filename,const char *const *_ArgList,const char *const *_Env);







       
       
       
       

#pragma pack(pop)

# 1 "C:/msys64/mingw64/include/sec_api/stdio_s.h" 1 3
# 9 "C:/msys64/mingw64/include/sec_api/stdio_s.h" 3
# 1 "C:/msys64/mingw64/include/stdio.h" 1 3
# 10 "C:/msys64/mingw64/include/sec_api/stdio_s.h" 2 3
# 29 "C:/msys64/mingw64/include/sec_api/stdio_s.h" 3
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) clearerr_s(FILE *_File);

  size_t __attribute__((__cdecl__)) fread_s(void *_DstBuf,size_t _DstSize,size_t _ElementSize,size_t _Count,FILE *_File);
# 494 "C:/msys64/mingw64/include/sec_api/stdio_s.h" 3
  int __attribute__((__cdecl__)) fprintf_s(FILE *_File,const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fscanf_s_l(FILE *_File,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) fscanf_s(FILE *_File, const char *_Format, ...);
  int __attribute__((__cdecl__)) printf_s(const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scanf_l(const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scanf_s_l(const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) scanf_s(const char *_Format, ...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snprintf_c(char *_DstBuf,size_t _MaxCount,const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnprintf_c(char *_DstBuf,size_t _MaxCount,const char *_Format,va_list _ArgList);

  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fscanf_l(FILE *_File,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _sscanf_l(const char *_Src,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _sscanf_s_l(const char *_Src,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) sscanf_s(const char *_Src,const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snscanf_s(const char *_Src,size_t _MaxCount,const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snscanf_l(const char *_Src,size_t _MaxCount,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snscanf_s_l(const char *_Src,size_t _MaxCount,const char *_Format,_locale_t _Locale,...);
  int __attribute__((__cdecl__)) vfprintf_s(FILE *_File,const char *_Format,va_list _ArgList);
  int __attribute__((__cdecl__)) vprintf_s(const char *_Format,va_list _ArgList);

  int __attribute__((__cdecl__)) vsnprintf_s(char *_DstBuf,size_t _DstSize,size_t _MaxCount,const char *_Format,va_list _ArgList);

  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnprintf_s(char *_DstBuf,size_t _DstSize,size_t _MaxCount,const char *_Format,va_list _ArgList);

  __attribute__((dllimport)) int __attribute__((__cdecl__)) vsprintf_s(char *_DstBuf,size_t _Size,const char *_Format,va_list _ArgList);

  __attribute__((dllimport)) int __attribute__((__cdecl__)) sprintf_s(char *_DstBuf,size_t _DstSize,const char *_Format,...);

  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snprintf_s(char *_DstBuf,size_t _DstSize,size_t _MaxCount,const char *_Format,...);

  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fprintf_p(FILE *_File,const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _printf_p(const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _sprintf_p(char *_Dst,size_t _MaxCount,const char *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfprintf_p(FILE *_File,const char *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vprintf_p(const char *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsprintf_p(char *_Dst,size_t _MaxCount,const char *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scprintf_p(const char *_Format,...);
  __attribute__((dllimport)) int __attribute__((__cdecl__)) _vscprintf_p(const char *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _printf_l(const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _printf_p_l(const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vprintf_l(const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vprintf_p_l(const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fprintf_l(FILE *_File,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fprintf_p_l(FILE *_File,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfprintf_l(FILE *_File,const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfprintf_p_l(FILE *_File,const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _sprintf_l(char *_DstBuf,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _sprintf_p_l(char *_DstBuf,size_t _MaxCount,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsprintf_l(char *_DstBuf,const char *_Format,_locale_t,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsprintf_p_l(char *_DstBuf,size_t _MaxCount,const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scprintf_l(const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scprintf_p_l(const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vscprintf_l(const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vscprintf_p_l(const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _printf_s_l(const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vprintf_s_l(const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fprintf_s_l(FILE *_File,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfprintf_s_l(FILE *_File,const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _sprintf_s_l(char *_DstBuf,size_t _DstSize,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsprintf_s_l(char *_DstBuf,size_t _DstSize,const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snprintf_s_l(char *_DstBuf,size_t _DstSize,size_t _MaxCount,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnprintf_s_l(char *_DstBuf,size_t _DstSize,size_t _MaxCount,const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snprintf_l(char *_DstBuf,size_t _MaxCount,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snprintf_c_l(char *_DstBuf,size_t _MaxCount,const char *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnprintf_l(char *_DstBuf,size_t _MaxCount,const char *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnprintf_c_l(char *_DstBuf,size_t _MaxCount,const char *,_locale_t _Locale,va_list _ArgList);


 
 
 
 
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) fopen_s(FILE **_File,const char *_Filename,const char *_Mode);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) freopen_s(FILE** _File, const char *_Filename, const char *_Mode, FILE *_Stream);

  __attribute__ ((__dllimport__)) char* __attribute__((__cdecl__)) gets_s(char*,rsize_t);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) tmpfile_s(FILE **_File);

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) tmpnam_s(char*,rsize_t);
 




  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _getws_s(wchar_t *_Str,size_t _SizeInWords);
 
# 788 "C:/msys64/mingw64/include/sec_api/stdio_s.h" 3
  int __attribute__((__cdecl__)) fwprintf_s(FILE *_File,const wchar_t *_Format,...);
  int __attribute__((__cdecl__)) wprintf_s(const wchar_t *_Format,...);
  int __attribute__((__cdecl__)) vfwprintf_s(FILE *_File,const wchar_t *_Format,va_list _ArgList);
  int __attribute__((__cdecl__)) vwprintf_s(const wchar_t *_Format,va_list _ArgList);

  int __attribute__((__cdecl__)) vswprintf_s(wchar_t *_Dst,size_t _SizeInWords,const wchar_t *_Format,va_list _ArgList);

  int __attribute__((__cdecl__)) swprintf_s(wchar_t *_Dst,size_t _SizeInWords,const wchar_t *_Format,...);

  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnwprintf_s(wchar_t *_DstBuf,size_t _DstSizeInWords,size_t _MaxCount,const wchar_t *_Format,va_list _ArgList);

  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwprintf_s(wchar_t *_DstBuf,size_t _DstSizeInWords,size_t _MaxCount,const wchar_t *_Format,...);


  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wprintf_s_l(const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vwprintf_s_l(const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fwprintf_s_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfwprintf_s_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swprintf_s_l(wchar_t *_DstBuf,size_t _DstSize,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vswprintf_s_l(wchar_t *_DstBuf,size_t _DstSize,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwprintf_s_l(wchar_t *_DstBuf,size_t _DstSize,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnwprintf_s_l(wchar_t *_DstBuf,size_t _DstSize,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fwscanf_s_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) fwscanf_s(FILE *_File, const wchar_t *_Format, ...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swscanf_s_l(const wchar_t *_Src,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) swscanf_s(const wchar_t *_Src,const wchar_t *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwscanf_s(const wchar_t *_Src,size_t _MaxCount,const wchar_t *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwscanf_s_l(const wchar_t *_Src,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wscanf_s_l(const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) wscanf_s(const wchar_t *_Format, ...);


 
 
 
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wfopen_s(FILE **_File,const wchar_t *_Filename,const wchar_t *_Mode);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wfreopen_s(FILE **_File,const wchar_t *_Filename,const wchar_t *_Mode,FILE *_OldFile);

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wtmpnam_s(wchar_t *_DstBuf,size_t _SizeInWords);
 


  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fwprintf_p(FILE *_File,const wchar_t *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wprintf_p(const wchar_t *_Format,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfwprintf_p(FILE *_File,const wchar_t *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vwprintf_p(const wchar_t *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swprintf_p(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,...);
  __attribute__((dllimport)) int __attribute__((__cdecl__)) _vswprintf_p(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scwprintf_p(const wchar_t *_Format,...);
  __attribute__((dllimport)) int __attribute__((__cdecl__)) _vscwprintf_p(const wchar_t *_Format,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wprintf_l(const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wprintf_p_l(const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vwprintf_l(const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vwprintf_p_l(const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fwprintf_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fwprintf_p_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfwprintf_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vfwprintf_p_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swprintf_c_l(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swprintf_p_l(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vswprintf_c_l(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vswprintf_p_l(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scwprintf_l(const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _scwprintf_p_l(const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vscwprintf_p_l(const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwprintf_l(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vsnwprintf_l(wchar_t *_DstBuf,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) __swprintf_l(wchar_t *_Dest,const wchar_t *_Format,_locale_t _Plocinfo,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) __vswprintf_l(wchar_t *_Dest,const wchar_t *_Format,_locale_t _Plocinfo,va_list _Args);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _vscwprintf_l(const wchar_t *_Format,_locale_t _Locale,va_list _ArgList);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _fwscanf_l(FILE *_File,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _swscanf_l(const wchar_t *_Src,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _snwscanf_l(const wchar_t *_Src,size_t _MaxCount,const wchar_t *_Format,_locale_t _Locale,...);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wscanf_l(const wchar_t *_Format,_locale_t _Locale,...);
# 1639 "C:/msys64/mingw64/include/stdio.h" 2 3
# 16 "lvm.c" 2
# 1 "C:/msys64/mingw64/include/stdlib.h" 1 3
# 10 "C:/msys64/mingw64/include/stdlib.h" 3
# 1 "C:/msys64/mingw64/include/corecrt_wstdlib.h" 1 3
# 15 "C:/msys64/mingw64/include/corecrt_wstdlib.h" 3
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _itow_s (int _Val,wchar_t *_DstBuf,size_t _SizeInWords,int _Radix);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _ltow_s (long _Val,wchar_t *_DstBuf,size_t _SizeInWords,int _Radix);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _ultow_s (unsigned long _Val,wchar_t *_DstBuf,size_t _SizeInWords,int _Radix);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wgetenv_s(size_t *_ReturnSize,wchar_t *_DstBuf,size_t _DstSizeInWords,const wchar_t *_VarName);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wdupenv_s(wchar_t **_Buffer,size_t *_BufferSizeInWords,const wchar_t *_VarName);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _i64tow_s(long long _Val,wchar_t *_DstBuf,size_t _SizeInWords,int _Radix);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _ui64tow_s(unsigned long long _Val,wchar_t *_DstBuf,size_t _SizeInWords,int _Radix);

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wmakepath_s(wchar_t *_PathResult,size_t _SizeInWords,const wchar_t *_Drive,const wchar_t *_Dir,const wchar_t *_Filename,const wchar_t *_Ext);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wputenv_s(const wchar_t *_Name,const wchar_t *_Value);

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wsearchenv_s(const wchar_t *_Filename,const wchar_t *_EnvVar,wchar_t *_ResultPath,size_t _SizeInWords);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wsplitpath_s(const wchar_t *_FullPath,wchar_t *_Drive,size_t _DriveSizeInWords,wchar_t *_Dir,size_t _DirSizeInWords,wchar_t *_Filename,size_t _FilenameSizeInWords,wchar_t *_Ext,size_t _ExtSizeInWords);
 
# 11 "C:/msys64/mingw64/include/stdlib.h" 2 3
# 1 "C:/msys64/mingw64/include/limits.h" 1 3
# 12 "C:/msys64/mingw64/include/stdlib.h" 2 3
# 26 "C:/msys64/mingw64/include/stdlib.h" 3
#pragma pack(push,_CRT_PACKING)
# 50 "C:/msys64/mingw64/include/stdlib.h" 3
  typedef int (__attribute__((__cdecl__)) *_onexit_t)(void);
# 60 "C:/msys64/mingw64/include/stdlib.h" 3
  typedef struct _div_t {
    int quot;
    int rem;
  } div_t;

  typedef struct _ldiv_t {
    long quot;
    long rem;
  } ldiv_t;





#pragma pack(4)
  typedef struct {
    unsigned char ld[10];
  } _LDOUBLE;
#pragma pack()



  typedef struct {
    double x;
  } _CRT_DOUBLE;

  typedef struct {
    float f;
  } _CRT_FLOAT;

       


  typedef struct {
    long double x;
  } _LONGDOUBLE;

       

#pragma pack(4)
  typedef struct {
    unsigned char ld12[12];
  } _LDBL12;
#pragma pack()
# 116 "C:/msys64/mingw64/include/stdlib.h" 3
  extern int * __imp___mb_cur_max;




__attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) ___mb_cur_max_func(void);
# 143 "C:/msys64/mingw64/include/stdlib.h" 3
  typedef void (__attribute__((__cdecl__)) *_purecall_handler)(void);

  __attribute__ ((__dllimport__)) _purecall_handler __attribute__((__cdecl__)) _set_purecall_handler(_purecall_handler _Handler);
  __attribute__ ((__dllimport__)) _purecall_handler __attribute__((__cdecl__)) _get_purecall_handler(void);

  typedef void (__attribute__((__cdecl__)) *_invalid_parameter_handler)(const wchar_t *,const wchar_t *,const wchar_t *,unsigned int,uintptr_t);
  __attribute__ ((__dllimport__)) _invalid_parameter_handler __attribute__((__cdecl__)) _set_invalid_parameter_handler(_invalid_parameter_handler _Handler);
  __attribute__ ((__dllimport__)) _invalid_parameter_handler __attribute__((__cdecl__)) _get_invalid_parameter_handler(void);



  __attribute__ ((__dllimport__)) extern int *__attribute__((__cdecl__)) _errno(void);

  errno_t __attribute__((__cdecl__)) _set_errno(int _Value);
  errno_t __attribute__((__cdecl__)) _get_errno(int *_Value);

  __attribute__ ((__dllimport__)) unsigned long *__attribute__((__cdecl__)) __doserrno(void);

  errno_t __attribute__((__cdecl__)) _set_doserrno(unsigned long _Value);
  errno_t __attribute__((__cdecl__)) _get_doserrno(unsigned long *_Value);
# 173 "C:/msys64/mingw64/include/stdlib.h" 3
  extern __attribute__((dllimport)) char *_sys_errlist[1];
  extern __attribute__((dllimport)) int _sys_nerr;





  __attribute__ ((__dllimport__)) char ***__attribute__((__cdecl__)) __p___argv(void);
  __attribute__ ((__dllimport__)) int *__attribute__((__cdecl__)) __p__fmode(void);
# 191 "C:/msys64/mingw64/include/stdlib.h" 3
  errno_t __attribute__((__cdecl__)) _get_pgmptr(char **_Value);
  errno_t __attribute__((__cdecl__)) _get_wpgmptr(wchar_t **_Value);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _set_fmode(int _Mode);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _get_fmode(int *_PMode);
# 282 "C:/msys64/mingw64/include/stdlib.h" 3
  extern int * __imp___argc;



  extern char *** __imp___argv;



  extern wchar_t *** __imp___wargv;
# 322 "C:/msys64/mingw64/include/stdlib.h" 3
  extern char *** __imp__environ;




  extern wchar_t *** __imp__wenviron;






  extern char ** __imp__pgmptr;




  extern wchar_t ** __imp__wpgmptr;




  extern unsigned int * __imp__osplatform;




  extern unsigned int * __imp__osver;




  extern unsigned int * __imp__winver;




  extern unsigned int * __imp__winmajor;




  extern unsigned int * __imp__winminor;





  errno_t __attribute__((__cdecl__)) _get_osplatform(unsigned int *_Value);
  errno_t __attribute__((__cdecl__)) _get_osver(unsigned int *_Value);
  errno_t __attribute__((__cdecl__)) _get_winver(unsigned int *_Value);
  errno_t __attribute__((__cdecl__)) _get_winmajor(unsigned int *_Value);
  errno_t __attribute__((__cdecl__)) _get_winminor(unsigned int *_Value);
# 388 "C:/msys64/mingw64/include/stdlib.h" 3
  void __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) exit(int _Code) __attribute__ ((__noreturn__));
  void __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) _exit(int _Code) __attribute__ ((__noreturn__));






  void __attribute__((__cdecl__)) _Exit(int) __attribute__ ((__noreturn__));






       

  void __attribute__((__cdecl__)) __attribute__ ((__noreturn__)) abort(void);
       



  __attribute__ ((__dllimport__)) unsigned int __attribute__((__cdecl__)) _set_abort_behavior(unsigned int _Flags,unsigned int _Mask);







  __extension__ long long __attribute__((__cdecl__)) _abs64(long long);

  extern __inline__ __attribute__((__always_inline__,__gnu_inline__)) long long __attribute__((__cdecl__)) _abs64(long long x) {
    return __builtin_llabs(x);
  }


  int __attribute__((__cdecl__)) atexit(void (__attribute__((__cdecl__)) *)(void));
# 434 "C:/msys64/mingw64/include/stdlib.h" 3
  int __attribute__((__cdecl__)) atoi(const char *_Str);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _atoi_l(const char *_Str,_locale_t _Locale);
  long __attribute__((__cdecl__)) atol(const char *_Str);
  __attribute__ ((__dllimport__)) long __attribute__((__cdecl__)) _atol_l(const char *_Str,_locale_t _Locale);


  void *__attribute__((__cdecl__)) bsearch(const void *_Key,const void *_Base,size_t _NumOfElements,size_t _SizeOfElements,int (__attribute__((__cdecl__)) *_PtFuncCompare)(const void *,const void *));
  void __attribute__((__cdecl__)) qsort(void *_Base,size_t _NumOfElements,size_t _SizeOfElements,int (__attribute__((__cdecl__)) *_PtFuncCompare)(const void *,const void *));

  unsigned short __attribute__((__cdecl__)) _byteswap_ushort(unsigned short _Short);
  unsigned long __attribute__((__cdecl__)) _byteswap_ulong (unsigned long _Long);
  __extension__ unsigned long long __attribute__((__cdecl__)) _byteswap_uint64(unsigned long long _Int64);
  div_t __attribute__((__cdecl__)) div(int _Numerator,int _Denominator);
  char *__attribute__((__cdecl__)) getenv(const char *_VarName) ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _itoa(int _Value,char *_Dest,int _Radix);
  __extension__ __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _i64toa(long long _Val,char *_DstBuf,int _Radix) ;
  __extension__ __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _ui64toa(unsigned long long _Val,char *_DstBuf,int _Radix) ;
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _atoi64(const char *_String);
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _atoi64_l(const char *_String,_locale_t _Locale);
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _strtoi64(const char *_String,char **_EndPtr,int _Radix);
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _strtoi64_l(const char *_String,char **_EndPtr,int _Radix,_locale_t _Locale);
  __extension__ __attribute__ ((__dllimport__)) unsigned long long __attribute__((__cdecl__)) _strtoui64(const char *_String,char **_EndPtr,int _Radix);
  __extension__ __attribute__ ((__dllimport__)) unsigned long long __attribute__((__cdecl__)) _strtoui64_l(const char *_String,char **_EndPtr,int _Radix,_locale_t _Locale);
  ldiv_t __attribute__((__cdecl__)) ldiv(long _Numerator,long _Denominator);
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _ltoa(long _Value,char *_Dest,int _Radix) ;
  int __attribute__((__cdecl__)) mblen(const char *_Ch,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _mblen_l(const char *_Ch,size_t _MaxCount,_locale_t _Locale);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _mbstrlen(const char *_Str);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _mbstrlen_l(const char *_Str,_locale_t _Locale);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _mbstrnlen(const char *_Str,size_t _MaxCount);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _mbstrnlen_l(const char *_Str,size_t _MaxCount,_locale_t _Locale);
  int __attribute__((__cdecl__)) mbtowc(wchar_t * __restrict__ _DstCh,const char * __restrict__ _SrcCh,size_t _SrcSizeInBytes);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _mbtowc_l(wchar_t * __restrict__ _DstCh,const char * __restrict__ _SrcCh,size_t _SrcSizeInBytes,_locale_t _Locale);
  size_t __attribute__((__cdecl__)) mbstowcs(wchar_t * __restrict__ _Dest,const char * __restrict__ _Source,size_t _MaxCount);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _mbstowcs_l(wchar_t * __restrict__ _Dest,const char * __restrict__ _Source,size_t _MaxCount,_locale_t _Locale);
  int __attribute__((__cdecl__)) mkstemp(char *template_name);
  int __attribute__((__cdecl__)) rand(void);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _set_error_mode(int _Mode);
  void __attribute__((__cdecl__)) srand(unsigned int _Seed);
# 483 "C:/msys64/mingw64/include/stdlib.h" 3
static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
double __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) strtod(const char * __restrict__ _Str,char ** __restrict__ _EndPtr)
{
  double __attribute__((__cdecl__)) __mingw_strtod (const char * __restrict__, char ** __restrict__);
  return __mingw_strtod( _Str, _EndPtr);
}

static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
float __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) strtof(const char * __restrict__ _Str,char ** __restrict__ _EndPtr)
{
  float __attribute__((__cdecl__)) __mingw_strtof (const char * __restrict__, char ** __restrict__);
  return __mingw_strtof( _Str, _EndPtr);
}






  long double __attribute__((__cdecl__)) __attribute__ ((__nothrow__)) strtold(const char * __restrict__ , char ** __restrict__ );


  extern double __attribute__((__cdecl__)) __attribute__ ((__nothrow__))
  __strtod (const char * __restrict__ , char ** __restrict__);







  float __attribute__((__cdecl__)) __mingw_strtof (const char * __restrict__, char ** __restrict__);
  double __attribute__((__cdecl__)) __mingw_strtod (const char * __restrict__, char ** __restrict__);
  long double __attribute__((__cdecl__)) __mingw_strtold(const char * __restrict__, char ** __restrict__);

  __attribute__ ((__dllimport__)) float __attribute__((__cdecl__)) _strtof_l(const char * __restrict__ _Str,char ** __restrict__ _EndPtr,_locale_t _Locale);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _strtod_l(const char * __restrict__ _Str,char ** __restrict__ _EndPtr,_locale_t _Locale);
  long __attribute__((__cdecl__)) strtol(const char * __restrict__ _Str,char ** __restrict__ _EndPtr,int _Radix);
  __attribute__ ((__dllimport__)) long __attribute__((__cdecl__)) _strtol_l(const char * __restrict__ _Str,char ** __restrict__ _EndPtr,int _Radix,_locale_t _Locale);
  unsigned long __attribute__((__cdecl__)) strtoul(const char * __restrict__ _Str,char ** __restrict__ _EndPtr,int _Radix);
  __attribute__ ((__dllimport__)) unsigned long __attribute__((__cdecl__)) _strtoul_l(const char * __restrict__ _Str,char ** __restrict__ _EndPtr,int _Radix,_locale_t _Locale);


  int __attribute__((__cdecl__)) system(const char *_Command);

  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _ultoa(unsigned long _Value,char *_Dest,int _Radix) ;
  int __attribute__((__cdecl__)) wctomb(char *_MbCh,wchar_t _WCh) ;
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wctomb_l(char *_MbCh,wchar_t _WCh,_locale_t _Locale) ;
  size_t __attribute__((__cdecl__)) wcstombs(char * __restrict__ _Dest,const wchar_t * __restrict__ _Source,size_t _MaxCount) ;
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _wcstombs_l(char * __restrict__ _Dest,const wchar_t * __restrict__ _Source,size_t _MaxCount,_locale_t _Locale) ;



  void *__attribute__((__cdecl__)) calloc(size_t _NumOfElements,size_t _SizeOfElements);
  void __attribute__((__cdecl__)) free(void *_Memory);
  void *__attribute__((__cdecl__)) malloc(size_t _Size);
  void *__attribute__((__cdecl__)) realloc(void *_Memory,size_t _NewSize);
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _aligned_free(void *_Memory);
  __attribute__ ((__dllimport__)) void *__attribute__((__cdecl__)) _aligned_malloc(size_t _Size,size_t _Alignment);
  __attribute__ ((__dllimport__)) void *__attribute__((__cdecl__)) _aligned_offset_malloc(size_t _Size,size_t _Alignment,size_t _Offset);
  __attribute__ ((__dllimport__)) void *__attribute__((__cdecl__)) _aligned_realloc(void *_Memory,size_t _Size,size_t _Alignment);
  __attribute__ ((__dllimport__)) void *__attribute__((__cdecl__)) _aligned_offset_realloc(void *_Memory,size_t _Size,size_t _Alignment,size_t _Offset);
# 555 "C:/msys64/mingw64/include/stdlib.h" 3
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _itow(int _Value,wchar_t *_Dest,int _Radix) ;
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _ltow(long _Value,wchar_t *_Dest,int _Radix) ;
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _ultow(unsigned long _Value,wchar_t *_Dest,int _Radix) ;

  double __attribute__((__cdecl__)) __mingw_wcstod(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr);
  float __attribute__((__cdecl__)) __mingw_wcstof(const wchar_t * __restrict__ nptr, wchar_t ** __restrict__ endptr);
  long double __attribute__((__cdecl__)) __mingw_wcstold(const wchar_t * __restrict__, wchar_t ** __restrict__);


  static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
  double __attribute__((__cdecl__)) wcstod(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr){
    return __mingw_wcstod(_Str,_EndPtr);
  }
  static __attribute__ ((__unused__)) __inline__ __attribute__((__cdecl__))
  float __attribute__((__cdecl__)) wcstof(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr){
    return __mingw_wcstof(_Str,_EndPtr);
  }






  long double __attribute__((__cdecl__)) wcstold(const wchar_t * __restrict__, wchar_t ** __restrict__);

  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _wcstod_l(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr,_locale_t _Locale);
  __attribute__ ((__dllimport__)) float __attribute__((__cdecl__)) _wcstof_l(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr,_locale_t _Locale);
  long __attribute__((__cdecl__)) wcstol(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr,int _Radix);
  __attribute__ ((__dllimport__)) long __attribute__((__cdecl__)) _wcstol_l(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr,int _Radix,_locale_t _Locale);
  unsigned long __attribute__((__cdecl__)) wcstoul(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr,int _Radix);
  __attribute__ ((__dllimport__)) unsigned long __attribute__((__cdecl__)) _wcstoul_l(const wchar_t * __restrict__ _Str,wchar_t ** __restrict__ _EndPtr,int _Radix,_locale_t _Locale);
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wgetenv(const wchar_t *_VarName) ;


  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wsystem(const wchar_t *_Command);

  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _wtof(const wchar_t *_Str);
  __attribute__ ((__dllimport__)) double __attribute__((__cdecl__)) _wtof_l(const wchar_t *_Str,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wtoi(const wchar_t *_Str);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wtoi_l(const wchar_t *_Str,_locale_t _Locale);
  __attribute__ ((__dllimport__)) long __attribute__((__cdecl__)) _wtol(const wchar_t *_Str);
  __attribute__ ((__dllimport__)) long __attribute__((__cdecl__)) _wtol_l(const wchar_t *_Str,_locale_t _Locale);

  __extension__ __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _i64tow(long long _Val,wchar_t *_DstBuf,int _Radix) ;
  __extension__ __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _ui64tow(unsigned long long _Val,wchar_t *_DstBuf,int _Radix) ;
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _wtoi64(const wchar_t *_Str);
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _wtoi64_l(const wchar_t *_Str,_locale_t _Locale);
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _wcstoi64(const wchar_t *_Str,wchar_t **_EndPtr,int _Radix);
  __extension__ __attribute__ ((__dllimport__)) long long __attribute__((__cdecl__)) _wcstoi64_l(const wchar_t *_Str,wchar_t **_EndPtr,int _Radix,_locale_t _Locale);
  __extension__ __attribute__ ((__dllimport__)) unsigned long long __attribute__((__cdecl__)) _wcstoui64(const wchar_t *_Str,wchar_t **_EndPtr,int _Radix);
  __extension__ __attribute__ ((__dllimport__)) unsigned long long __attribute__((__cdecl__)) _wcstoui64_l(const wchar_t *_Str ,wchar_t **_EndPtr,int _Radix,_locale_t _Locale);


  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _putenv(const char *_EnvString);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wputenv(const wchar_t *_EnvString);



  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _fullpath(char *_FullPath,const char *_Path,size_t _SizeInBytes);
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _ecvt(double _Val,int _NumOfDigits,int *_PtDec,int *_PtSign) ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _fcvt(double _Val,int _NumOfDec,int *_PtDec,int *_PtSign) ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _gcvt(double _Val,int _NumOfDigits,char *_DstBuf) ;
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _atodbl(_CRT_DOUBLE *_Result,char *_Str);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _atoldbl(_LDOUBLE *_Result,char *_Str);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _atoflt(_CRT_FLOAT *_Result,char *_Str);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _atodbl_l(_CRT_DOUBLE *_Result,char *_Str,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _atoldbl_l(_LDOUBLE *_Result,char *_Str,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _atoflt_l(_CRT_FLOAT *_Result,char *_Str,_locale_t _Locale);
# 638 "C:/msys64/mingw64/include/stdlib.h" 3
unsigned long __attribute__((__cdecl__)) _lrotl(unsigned long,int);
unsigned long __attribute__((__cdecl__)) _lrotr(unsigned long,int);





  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _makepath(char *_Path,const char *_Drive,const char *_Dir,const char *_Filename,const char *_Ext);
  _onexit_t __attribute__((__cdecl__)) _onexit(_onexit_t _Func);





       
       


  __extension__ unsigned long long __attribute__((__cdecl__)) _rotl64(unsigned long long _Val,int _Shift);
  __extension__ unsigned long long __attribute__((__cdecl__)) _rotr64(unsigned long long Value,int Shift);
       
       
       
       


  unsigned int __attribute__((__cdecl__)) _rotr(unsigned int _Val,int _Shift);
  unsigned int __attribute__((__cdecl__)) _rotl(unsigned int _Val,int _Shift);
       
       
  __extension__ unsigned long long __attribute__((__cdecl__)) _rotr64(unsigned long long _Val,int _Shift);
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _searchenv(const char *_Filename,const char *_EnvVar,char *_ResultPath) ;
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _splitpath(const char *_FullPath,char *_Drive,char *_Dir,char *_Filename,char *_Ext) ;
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _swab(char *_Buf1,char *_Buf2,int _SizeInBytes);



  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wfullpath(wchar_t *_FullPath,const wchar_t *_Path,size_t _SizeInWords);
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _wmakepath(wchar_t *_ResultPath,const wchar_t *_Drive,const wchar_t *_Dir,const wchar_t *_Filename,const wchar_t *_Ext);




  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _wsearchenv(const wchar_t *_Filename,const wchar_t *_EnvVar,wchar_t *_ResultPath) ;
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _wsplitpath(const wchar_t *_FullPath,wchar_t *_Drive,wchar_t *_Dir,wchar_t *_Filename,wchar_t *_Ext) ;


  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _beep(unsigned _Frequency,unsigned _Duration) __attribute__ ((__deprecated__));

  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _seterrormode(int _Mode) __attribute__ ((__deprecated__));
  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) _sleep(unsigned long _Duration) __attribute__ ((__deprecated__));
# 709 "C:/msys64/mingw64/include/stdlib.h" 3
  char *__attribute__((__cdecl__)) ecvt(double _Val,int _NumOfDigits,int *_PtDec,int *_PtSign) ;
  char *__attribute__((__cdecl__)) fcvt(double _Val,int _NumOfDec,int *_PtDec,int *_PtSign) ;
  char *__attribute__((__cdecl__)) gcvt(double _Val,int _NumOfDigits,char *_DstBuf) ;
  char *__attribute__((__cdecl__)) itoa(int _Val,char *_DstBuf,int _Radix) ;
  char *__attribute__((__cdecl__)) ltoa(long _Val,char *_DstBuf,int _Radix) ;
  int __attribute__((__cdecl__)) putenv(const char *_EnvString) ;



  void __attribute__((__cdecl__)) swab(char *_Buf1,char *_Buf2,int _SizeInBytes) ;


  char *__attribute__((__cdecl__)) ultoa(unsigned long _Val,char *_Dstbuf,int _Radix) ;
  _onexit_t __attribute__((__cdecl__)) onexit(_onexit_t _Func);





  typedef struct { __extension__ long long quot, rem; } lldiv_t;

  __extension__ lldiv_t __attribute__((__cdecl__)) lldiv(long long, long long);

  __extension__ long long __attribute__((__cdecl__)) llabs(long long);




  __extension__ long long __attribute__((__cdecl__)) strtoll(const char * __restrict__, char ** __restrict, int);
  __extension__ unsigned long long __attribute__((__cdecl__)) strtoull(const char * __restrict__, char ** __restrict__, int);


  __extension__ long long __attribute__((__cdecl__)) atoll (const char *);


  __extension__ long long __attribute__((__cdecl__)) wtoll (const wchar_t *);
  __extension__ char *__attribute__((__cdecl__)) lltoa (long long, char *, int);
  __extension__ char *__attribute__((__cdecl__)) ulltoa (unsigned long long , char *, int);
  __extension__ wchar_t *__attribute__((__cdecl__)) lltow (long long, wchar_t *, int);
  __extension__ wchar_t *__attribute__((__cdecl__)) ulltow (unsigned long long, wchar_t *, int);
# 766 "C:/msys64/mingw64/include/stdlib.h" 3
#pragma pack(pop)

# 1 "C:/msys64/mingw64/include/sec_api/stdlib_s.h" 1 3
# 9 "C:/msys64/mingw64/include/sec_api/stdlib_s.h" 3
# 1 "C:/msys64/mingw64/include/stdlib.h" 1 3
# 10 "C:/msys64/mingw64/include/sec_api/stdlib_s.h" 2 3





  __attribute__ ((__dllimport__)) void * __attribute__((__cdecl__)) bsearch_s(const void *_Key,const void *_Base,rsize_t _NumOfElements,rsize_t _SizeOfElements,int (__attribute__((__cdecl__)) * _PtFuncCompare)(void *, const void *, const void *), void *_Context);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _dupenv_s(char **_PBuffer,size_t *_PBufferSizeInBytes,const char *_VarName);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) getenv_s(size_t *_ReturnSize,char *_DstBuf,rsize_t _DstSize,const char *_VarName);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _itoa_s(int _Value,char *_DstBuf,size_t _Size,int _Radix);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _i64toa_s(long long _Val,char *_DstBuf,size_t _Size,int _Radix);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _ui64toa_s(unsigned long long _Val,char *_DstBuf,size_t _Size,int _Radix);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _ltoa_s(long _Val,char *_DstBuf,size_t _Size,int _Radix);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) mbstowcs_s(size_t *_PtNumOfCharConverted,wchar_t *_DstBuf,size_t _SizeInWords,const char *_SrcBuf,size_t _MaxCount);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _mbstowcs_s_l(size_t *_PtNumOfCharConverted,wchar_t *_DstBuf,size_t _SizeInWords,const char *_SrcBuf,size_t _MaxCount,_locale_t _Locale);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _ultoa_s(unsigned long _Val,char *_DstBuf,size_t _Size,int _Radix);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) wctomb_s(int *_SizeConverted,char *_MbCh,rsize_t _SizeInBytes,wchar_t _WCh);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wctomb_s_l(int *_SizeConverted,char *_MbCh,size_t _SizeInBytes,wchar_t _WCh,_locale_t _Locale);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) wcstombs_s(size_t *_PtNumOfCharConverted,char *_Dst,size_t _DstSizeInBytes,const wchar_t *_Src,size_t _MaxCountInBytes);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcstombs_s_l(size_t *_PtNumOfCharConverted,char *_Dst,size_t _DstSizeInBytes,const wchar_t *_Src,size_t _MaxCountInBytes,_locale_t _Locale);
 


  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _ecvt_s(char *_DstBuf,size_t _Size,double _Val,int _NumOfDights,int *_PtDec,int *_PtSign);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _fcvt_s(char *_DstBuf,size_t _Size,double _Val,int _NumOfDec,int *_PtDec,int *_PtSign);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _gcvt_s(char *_DstBuf,size_t _Size,double _Val,int _NumOfDigits);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _makepath_s(char *_PathResult,size_t _Size,const char *_Drive,const char *_Dir,const char *_Filename,const char *_Ext);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _putenv_s(const char *_Name,const char *_Value);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _searchenv_s(const char *_Filename,const char *_EnvVar,char *_ResultPath,size_t _SizeInBytes);

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _splitpath_s(const char *_FullPath,char *_Drive,size_t _DriveSize,char *_Dir,size_t _DirSize,char *_Filename,size_t _FilenameSize,char *_Ext,size_t _ExtSize);
 



  __attribute__ ((__dllimport__)) void __attribute__((__cdecl__)) qsort_s(void *_Base,size_t _NumOfElements,size_t _SizeOfElements,int (__attribute__((__cdecl__)) *_PtFuncCompare)(void *,const void *,const void *),void *_Context);
# 769 "C:/msys64/mingw64/include/stdlib.h" 2 3
# 1 "C:/msys64/mingw64/include/malloc.h" 1 3
# 11 "C:/msys64/mingw64/include/malloc.h" 3
#pragma pack(push,_CRT_PACKING)
# 46 "C:/msys64/mingw64/include/malloc.h" 3
  typedef struct _heapinfo {
    int *_pentry;
    size_t _size;
    int _useflag;
  } _HEAPINFO;


  extern unsigned int _amblksiz;
# 76 "C:/msys64/mingw64/include/malloc.h" 3
void * __mingw_aligned_malloc (size_t _Size, size_t _Alignment);
void __mingw_aligned_free (void *_Memory);
void * __mingw_aligned_offset_realloc (void *_Memory, size_t _Size, size_t _Alignment, size_t _Offset);
void * __mingw_aligned_realloc (void *_Memory, size_t _Size, size_t _Offset);



# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/mm_malloc.h" 1 3 4
# 29 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/mm_malloc.h" 3 4
# 1 "C:/msys64/mingw64/include/errno.h" 1 3 4
# 30 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/mm_malloc.h" 2 3 4


static __inline__ void *
_mm_malloc (size_t __size, size_t __align)
{
  void * __malloc_ptr;
  void * __aligned_ptr;


  if (__align & (__align - 1))
    {

      (*_errno()) = 22;

      return ((void *) 0);
    }

  if (__size == 0)
    return ((void *) 0);





    if (__align < 2 * sizeof (void *))
      __align = 2 * sizeof (void *);

  __malloc_ptr = malloc (__size + __align);
  if (!__malloc_ptr)
    return ((void *) 0);


  __aligned_ptr = (void *) (((size_t) __malloc_ptr + __align)
       & ~((size_t) (__align) - 1));


  ((void **) __aligned_ptr)[-1] = __malloc_ptr;

  return __aligned_ptr;
}

static __inline__ void
_mm_free (void *__aligned_ptr)
{
  if (__aligned_ptr)
    free (((void **) __aligned_ptr)[-1]);
}
# 84 "C:/msys64/mingw64/include/malloc.h" 2 3





  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _resetstkoflw (void);

  __attribute__ ((__dllimport__)) unsigned long __attribute__((__cdecl__)) _set_malloc_crt_max_wait(unsigned long _NewValue);

  __attribute__ ((__dllimport__)) void *__attribute__((__cdecl__)) _expand(void *_Memory,size_t _NewSize);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _msize(void *_Memory);






  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _get_sbh_threshold(void);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _set_sbh_threshold(size_t _NewValue);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _set_amblksiz(size_t _Value);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _get_amblksiz(size_t *_Value);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _heapadd(void *_Memory,size_t _Size);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _heapchk(void);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _heapmin(void);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _heapset(unsigned int _Fill);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _heapwalk(_HEAPINFO *_EntryInfo);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _heapused(size_t *_Used,size_t *_Commit);
  __attribute__ ((__dllimport__)) intptr_t __attribute__((__cdecl__)) _get_heap_handle(void);
# 124 "C:/msys64/mingw64/include/malloc.h" 3
  static __inline void *_MarkAllocaS(void *_Ptr,unsigned int _Marker) {
    if(_Ptr) {
      *((unsigned int*)_Ptr) = _Marker;
      _Ptr = (char*)_Ptr + 16;
    }
    return _Ptr;
  }
# 143 "C:/msys64/mingw64/include/malloc.h" 3
  static __inline void __attribute__((__cdecl__)) _freea(void *_Memory) {
    unsigned int _Marker;
    if(_Memory) {
      _Memory = (char*)_Memory - 16;
      _Marker = *(unsigned int *)_Memory;
      if(_Marker==0xDDDD) {
 free(_Memory);
      }





    }
  }
# 189 "C:/msys64/mingw64/include/malloc.h" 3
#pragma pack(pop)
# 770 "C:/msys64/mingw64/include/stdlib.h" 2 3
# 17 "lvm.c" 2
# 1 "C:/msys64/mingw64/include/string.h" 1 3
# 45 "C:/msys64/mingw64/include/string.h" 3
  __attribute__ ((__dllimport__)) void *__attribute__((__cdecl__)) _memccpy(void *_Dst,const void *_Src,int _Val,size_t _MaxCount);
  void *__attribute__((__cdecl__)) memchr(const void *_Buf ,int _Val,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _memicmp(const void *_Buf1,const void *_Buf2,size_t _Size);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _memicmp_l(const void *_Buf1,const void *_Buf2,size_t _Size,_locale_t _Locale);
  int __attribute__((__cdecl__)) memcmp(const void *_Buf1,const void *_Buf2,size_t _Size);
  void * __attribute__((__cdecl__)) memcpy(void * __restrict__ _Dst,const void * __restrict__ _Src,size_t _Size) ;
  __attribute__((dllimport)) errno_t __attribute__((__cdecl__)) memcpy_s (void *_dest,size_t _numberOfElements,const void *_src,size_t _count);
  void * __attribute__((__cdecl__)) mempcpy (void *_Dst, const void *_Src, size_t _Size);
  void * __attribute__((__cdecl__)) memset(void *_Dst,int _Val,size_t _Size);

  void * __attribute__((__cdecl__)) memccpy(void *_Dst,const void *_Src,int _Val,size_t _Size) ;
  int __attribute__((__cdecl__)) memicmp(const void *_Buf1,const void *_Buf2,size_t _Size) ;


  char * __attribute__((__cdecl__)) _strset(char *_Str,int _Val) ;
  char * __attribute__((__cdecl__)) _strset_l(char *_Str,int _Val,_locale_t _Locale) ;
  char * __attribute__((__cdecl__)) strcpy(char * __restrict__ _Dest,const char * __restrict__ _Source);
  char * __attribute__((__cdecl__)) strcat(char * __restrict__ _Dest,const char * __restrict__ _Source);
  int __attribute__((__cdecl__)) strcmp(const char *_Str1,const char *_Str2);
  size_t __attribute__((__cdecl__)) strlen(const char *_Str);
  size_t __attribute__((__cdecl__)) strnlen(const char *_Str,size_t _MaxCount);
  void *__attribute__((__cdecl__)) memmove(void *_Dst,const void *_Src,size_t _Size) ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strdup(const char *_Src);
  char *__attribute__((__cdecl__)) strchr(const char *_Str,int _Val);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _stricmp(const char *_Str1,const char *_Str2);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strcmpi(const char *_Str1,const char *_Str2);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _stricmp_l(const char *_Str1,const char *_Str2,_locale_t _Locale);
  int __attribute__((__cdecl__)) strcoll(const char *_Str1,const char *_Str2);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strcoll_l(const char *_Str1,const char *_Str2,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _stricoll(const char *_Str1,const char *_Str2);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _stricoll_l(const char *_Str1,const char *_Str2,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strncoll (const char *_Str1,const char *_Str2,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strncoll_l(const char *_Str1,const char *_Str2,size_t _MaxCount,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strnicoll (const char *_Str1,const char *_Str2,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strnicoll_l(const char *_Str1,const char *_Str2,size_t _MaxCount,_locale_t _Locale);
  size_t __attribute__((__cdecl__)) strcspn(const char *_Str,const char *_Control);
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strerror(const char *_ErrMsg) ;
  char *__attribute__((__cdecl__)) strerror(int) ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strlwr(char *_String) ;
  char *strlwr_l(char *_String,_locale_t _Locale) ;
  char *__attribute__((__cdecl__)) strncat(char * __restrict__ _Dest,const char * __restrict__ _Source,size_t _Count) ;
  int __attribute__((__cdecl__)) strncmp(const char *_Str1,const char *_Str2,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strnicmp(const char *_Str1,const char *_Str2,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _strnicmp_l(const char *_Str1,const char *_Str2,size_t _MaxCount,_locale_t _Locale);
  char *strncpy(char * __restrict__ _Dest,const char * __restrict__ _Source,size_t _Count) ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strnset(char *_Str,int _Val,size_t _MaxCount) ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strnset_l(char *str,int c,size_t count,_locale_t _Locale) ;
  char *__attribute__((__cdecl__)) strpbrk(const char *_Str,const char *_Control);
  char *__attribute__((__cdecl__)) strrchr(const char *_Str,int _Ch);
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strrev(char *_Str);
  size_t __attribute__((__cdecl__)) strspn(const char *_Str,const char *_Control);
  char *__attribute__((__cdecl__)) strstr(const char *_Str,const char *_SubStr);
  char *__attribute__((__cdecl__)) strtok(char * __restrict__ _Str,const char * __restrict__ _Delim) ;
       

  char *strtok_r(char * __restrict__ _Str, const char * __restrict__ _Delim, char ** __restrict__ __last);
       
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strupr(char *_String) ;
  __attribute__ ((__dllimport__)) char *_strupr_l(char *_String,_locale_t _Locale) ;
  size_t __attribute__((__cdecl__)) strxfrm(char * __restrict__ _Dst,const char * __restrict__ _Src,size_t _MaxCount);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _strxfrm_l(char * __restrict__ _Dst,const char * __restrict__ _Src,size_t _MaxCount,_locale_t _Locale);


  char *__attribute__((__cdecl__)) strdup(const char *_Src) ;
  int __attribute__((__cdecl__)) strcmpi(const char *_Str1,const char *_Str2) ;
  int __attribute__((__cdecl__)) stricmp(const char *_Str1,const char *_Str2) ;
  char *__attribute__((__cdecl__)) strlwr(char *_Str) ;
  int __attribute__((__cdecl__)) strnicmp(const char *_Str1,const char *_Str,size_t _MaxCount) ;
  int __attribute__((__cdecl__)) strncasecmp (const char *, const char *, size_t);
  int __attribute__((__cdecl__)) strcasecmp (const char *, const char *);







  char *__attribute__((__cdecl__)) strnset(char *_Str,int _Val,size_t _MaxCount) ;
  char *__attribute__((__cdecl__)) strrev(char *_Str) ;
  char *__attribute__((__cdecl__)) strset(char *_Str,int _Val) ;
  char *__attribute__((__cdecl__)) strupr(char *_Str) ;





  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcsdup(const wchar_t *_Str);
  wchar_t *__attribute__((__cdecl__)) wcscat(wchar_t * __restrict__ _Dest,const wchar_t * __restrict__ _Source) ;
  wchar_t *__attribute__((__cdecl__)) wcschr(const wchar_t *_Str,wchar_t _Ch);
  int __attribute__((__cdecl__)) wcscmp(const wchar_t *_Str1,const wchar_t *_Str2);
  wchar_t *__attribute__((__cdecl__)) wcscpy(wchar_t * __restrict__ _Dest,const wchar_t * __restrict__ _Source) ;
  size_t __attribute__((__cdecl__)) wcscspn(const wchar_t *_Str,const wchar_t *_Control);
  size_t __attribute__((__cdecl__)) wcslen(const wchar_t *_Str);
  size_t __attribute__((__cdecl__)) wcsnlen(const wchar_t *_Src,size_t _MaxCount);
  wchar_t *wcsncat(wchar_t * __restrict__ _Dest,const wchar_t * __restrict__ _Source,size_t _Count) ;
  int __attribute__((__cdecl__)) wcsncmp(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount);
  wchar_t *wcsncpy(wchar_t * __restrict__ _Dest,const wchar_t * __restrict__ _Source,size_t _Count) ;
  wchar_t *__attribute__((__cdecl__)) _wcsncpy_l(wchar_t * __restrict__ _Dest,const wchar_t * __restrict__ _Source,size_t _Count,_locale_t _Locale) ;
  wchar_t *__attribute__((__cdecl__)) wcspbrk(const wchar_t *_Str,const wchar_t *_Control);
  wchar_t *__attribute__((__cdecl__)) wcsrchr(const wchar_t *_Str,wchar_t _Ch);
  size_t __attribute__((__cdecl__)) wcsspn(const wchar_t *_Str,const wchar_t *_Control);
  wchar_t *__attribute__((__cdecl__)) wcsstr(const wchar_t *_Str,const wchar_t *_SubStr);



  wchar_t *__attribute__((__cdecl__)) wcstok(wchar_t * __restrict__ _Str,const wchar_t * __restrict__ _Delim) ;

  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcserror(int _ErrNum) ;
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) __wcserror(const wchar_t *_Str) ;
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsicmp(const wchar_t *_Str1,const wchar_t *_Str2);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsicmp_l(const wchar_t *_Str1,const wchar_t *_Str2,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsnicmp(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsnicmp_l(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount,_locale_t _Locale);
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcsnset(wchar_t *_Str,wchar_t _Val,size_t _MaxCount) ;
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcsrev(wchar_t *_Str);
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcsset(wchar_t *_Str,wchar_t _Val) ;
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcslwr(wchar_t *_String) ;
  __attribute__ ((__dllimport__)) wchar_t *_wcslwr_l(wchar_t *_String,_locale_t _Locale) ;
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcsupr(wchar_t *_String) ;
  __attribute__ ((__dllimport__)) wchar_t *_wcsupr_l(wchar_t *_String,_locale_t _Locale) ;
  size_t __attribute__((__cdecl__)) wcsxfrm(wchar_t * __restrict__ _Dst,const wchar_t * __restrict__ _Src,size_t _MaxCount);
  __attribute__ ((__dllimport__)) size_t __attribute__((__cdecl__)) _wcsxfrm_l(wchar_t * __restrict__ _Dst,const wchar_t * __restrict__ _Src,size_t _MaxCount,_locale_t _Locale);
  int __attribute__((__cdecl__)) wcscoll(const wchar_t *_Str1,const wchar_t *_Str2);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcscoll_l(const wchar_t *_Str1,const wchar_t *_Str2,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsicoll(const wchar_t *_Str1,const wchar_t *_Str2);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsicoll_l(const wchar_t *_Str1,const wchar_t *_Str2,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsncoll(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsncoll_l(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount,_locale_t _Locale);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsnicoll(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount);
  __attribute__ ((__dllimport__)) int __attribute__((__cdecl__)) _wcsnicoll_l(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount,_locale_t _Locale);


  wchar_t *__attribute__((__cdecl__)) wcsdup(const wchar_t *_Str) ;

  int __attribute__((__cdecl__)) wcsicmp(const wchar_t *_Str1,const wchar_t *_Str2) ;
  int __attribute__((__cdecl__)) wcsnicmp(const wchar_t *_Str1,const wchar_t *_Str2,size_t _MaxCount) ;
  wchar_t *__attribute__((__cdecl__)) wcsnset(wchar_t *_Str,wchar_t _Val,size_t _MaxCount) ;
  wchar_t *__attribute__((__cdecl__)) wcsrev(wchar_t *_Str) ;
  wchar_t *__attribute__((__cdecl__)) wcsset(wchar_t *_Str,wchar_t _Val) ;
  wchar_t *__attribute__((__cdecl__)) wcslwr(wchar_t *_Str) ;
  wchar_t *__attribute__((__cdecl__)) wcsupr(wchar_t *_Str) ;
  int __attribute__((__cdecl__)) wcsicoll(const wchar_t *_Str1,const wchar_t *_Str2) ;







# 1 "C:/msys64/mingw64/include/sec_api/string_s.h" 1 3
# 9 "C:/msys64/mingw64/include/sec_api/string_s.h" 3
# 1 "C:/msys64/mingw64/include/string.h" 1 3
# 10 "C:/msys64/mingw64/include/sec_api/string_s.h" 2 3
# 24 "C:/msys64/mingw64/include/sec_api/string_s.h" 3
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strset_s(char *_Dst,size_t _DstSize,int _Value);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strerror_s(char *_Buf,size_t _SizeInBytes,const char *_ErrMsg);
 
  __attribute__((dllimport)) errno_t __attribute__((__cdecl__)) strerror_s(char *_Buf,size_t _SizeInBytes,int _ErrNum);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strlwr_s(char *_Str,size_t _Size);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strlwr_s_l(char *_Str,size_t _Size,_locale_t _Locale);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strnset_s(char *_Str,size_t _Size,int _Val,size_t _MaxCount);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strupr_s(char *_Str,size_t _Size);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strupr_s_l(char *_Str,size_t _Size,_locale_t _Locale);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) strncat_s(char *_Dst,size_t _DstSizeInChars,const char *_Src,size_t _MaxCount);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strncat_s_l(char *_Dst,size_t _DstSizeInChars,const char *_Src,size_t _MaxCount,_locale_t _Locale);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) strcpy_s(char *_Dst, rsize_t _SizeInBytes, const char *_Src);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) strncpy_s(char *_Dst, size_t _DstSizeInChars, const char *_Src, size_t _MaxCount);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _strncpy_s_l(char *_Dst, size_t _DstSizeInChars, const char *_Src, size_t _MaxCount, _locale_t _Locale);
  ;
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) strtok_s(char *_Str,const char *_Delim,char **_Context);
  __attribute__ ((__dllimport__)) char *__attribute__((__cdecl__)) _strtok_s_l(char *_Str,const char *_Delim,char **_Context,_locale_t _Locale);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) strcat_s(char *_Dst, rsize_t _SizeInBytes, const char * _Src);
 

  extern __inline__ __attribute__((__always_inline__,__gnu_inline__)) size_t __attribute__((__cdecl__)) strnlen_s(const char * _src, size_t _count) {
    return _src ? strnlen(_src, _count) : 0;
  }

  __attribute__((dllimport)) errno_t __attribute__((__cdecl__)) memmove_s(void *_dest,size_t _numberOfElements,const void *_src,size_t _count);


  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) wcstok_s(wchar_t *_Str,const wchar_t *_Delim,wchar_t **_Context);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcserror_s(wchar_t *_Buf,size_t _SizeInWords,int _ErrNum);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) __wcserror_s(wchar_t *_Buffer,size_t _SizeInWords,const wchar_t *_ErrMsg);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsnset_s(wchar_t *_Dst,size_t _DstSizeInWords,wchar_t _Val,size_t _MaxCount);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsset_s(wchar_t *_Str,size_t _SizeInWords,wchar_t _Val);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcslwr_s(wchar_t *_Str,size_t _SizeInWords);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcslwr_s_l(wchar_t *_Str,size_t _SizeInWords,_locale_t _Locale);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsupr_s(wchar_t *_Str,size_t _Size);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsupr_s_l(wchar_t *_Str,size_t _Size,_locale_t _Locale);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) wcscpy_s(wchar_t *_Dst, rsize_t _SizeInWords, const wchar_t *_Src);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) wcscat_s(wchar_t * _Dst, rsize_t _SizeInWords, const wchar_t *_Src);
 

  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) wcsncat_s(wchar_t *_Dst,size_t _DstSizeInChars,const wchar_t *_Src,size_t _MaxCount);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsncat_s_l(wchar_t *_Dst,size_t _DstSizeInChars,const wchar_t *_Src,size_t _MaxCount,_locale_t _Locale);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) wcsncpy_s(wchar_t *_Dst, size_t _DstSizeInChars, const wchar_t *_Src, size_t _MaxCount);
  ;
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsncpy_s_l(wchar_t *_Dst, size_t _DstSizeInChars, const wchar_t *_Src, size_t _MaxCount, _locale_t _Locale);
  ;
  __attribute__ ((__dllimport__)) wchar_t *__attribute__((__cdecl__)) _wcstok_s_l(wchar_t *_Str,const wchar_t *_Delim,wchar_t **_Context,_locale_t _Locale);
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsset_s_l(wchar_t *_Str,size_t _SizeInChars,wchar_t _Val,_locale_t _Locale);
 
  __attribute__ ((__dllimport__)) errno_t __attribute__((__cdecl__)) _wcsnset_s_l(wchar_t *_Str,size_t _SizeInChars,wchar_t _Val, size_t _Count,_locale_t _Locale);
 

  extern __inline__ __attribute__((__always_inline__,__gnu_inline__)) size_t __attribute__((__cdecl__)) wcsnlen_s(const wchar_t * _src, size_t _count) {
    return _src ? wcsnlen(_src, _count) : 0;
  }
# 195 "C:/msys64/mingw64/include/string.h" 2 3
# 18 "lvm.c" 2

# 1 "lua.h" 1
# 12 "lua.h"
# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stdarg.h" 1 3 4
# 1 "C:/msys64/mingw64/include/stdarg.h" 1 3 4
# 140 "C:/msys64/mingw64/include/stdarg.h" 3 4
# 1 "C:/msys64/mingw64/include/_mingw_stdarg.h" 1 3 4
# 141 "C:/msys64/mingw64/include/stdarg.h" 2 3 4
# 2 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stdarg.h" 2 3 4
# 13 "lua.h" 2
# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 1 3 4
# 1 "C:/msys64/mingw64/include/stddef.h" 1 3 4
# 24 "C:/msys64/mingw64/include/stddef.h" 3 4
  __attribute__ ((__dllimport__)) extern unsigned long __attribute__((__cdecl__)) __threadid(void);

  __attribute__ ((__dllimport__)) extern uintptr_t __attribute__((__cdecl__)) __threadhandle(void);
# 424 "C:/msys64/mingw64/include/stddef.h" 3 4
typedef struct {
  long long __max_align_ll __attribute__((__aligned__(__alignof__(long long))));
  long double __max_align_ld __attribute__((__aligned__(__alignof__(long double))));
} max_align_t;
# 2 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 2 3 4
# 14 "lua.h" 2


# 1 "luaconf.h" 1
# 11 "luaconf.h"
# 1 "C:/msys64/mingw64/include/limits.h" 1 3
# 12 "luaconf.h" 2
# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 1 3 4
# 1 "C:/msys64/mingw64/include/stddef.h" 1 3 4
# 2 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 2 3 4
# 13 "luaconf.h" 2
# 17 "lua.h" 2
# 57 "lua.h"

# 57 "lua.h"
typedef struct lua_State lua_State;
# 90 "lua.h"
typedef double lua_Number;



typedef long long lua_Integer;


typedef unsigned long long lua_Unsigned;


typedef ptrdiff_t lua_KContext;





typedef int (*lua_CFunction) (lua_State *L);




typedef int (*lua_KFunction) (lua_State *L, int status, lua_KContext ctx);





typedef const char * (*lua_Reader) (lua_State *L, void *ud, size_t *sz);

typedef int (*lua_Writer) (lua_State *L, const void *p, size_t sz, void *ud);





typedef void * (*lua_Alloc) (void *ud, void *ptr, size_t osize, size_t nsize);





typedef void (*lua_WarnFunction) (void *ud, const char *msg, int tocont);





typedef struct lua_Debug lua_Debug;





typedef void (*lua_Hook) (lua_State *L, lua_Debug *ar);
# 157 "lua.h"
extern const char lua_ident[];





extern lua_State *(lua_newstate) (lua_Alloc f, void *ud);
extern void (lua_close) (lua_State *L);
extern lua_State *(lua_newthread) (lua_State *L);
extern int (lua_closethread) (lua_State *L, lua_State *from);
extern int (lua_resetthread) (lua_State *L);

extern lua_CFunction (lua_atpanic) (lua_State *L, lua_CFunction panicf);


extern lua_Number (lua_version) (lua_State *L);





extern int (lua_absindex) (lua_State *L, int idx);
extern int (lua_gettop) (lua_State *L);
extern void (lua_settop) (lua_State *L, int idx);
extern void (lua_pushvalue) (lua_State *L, int idx);
extern void (lua_rotate) (lua_State *L, int idx, int n);
extern void (lua_copy) (lua_State *L, int fromidx, int toidx);
extern int (lua_checkstack) (lua_State *L, int n);

extern void (lua_xmove) (lua_State *from, lua_State *to, int n);






extern int (lua_isnumber) (lua_State *L, int idx);
extern int (lua_isstring) (lua_State *L, int idx);
extern int (lua_iscfunction) (lua_State *L, int idx);
extern int (lua_isinteger) (lua_State *L, int idx);
extern int (lua_isuserdata) (lua_State *L, int idx);
extern int (lua_type) (lua_State *L, int idx);
extern const char *(lua_typename) (lua_State *L, int tp);

extern lua_Number (lua_tonumberx) (lua_State *L, int idx, int *isnum);
extern lua_Integer (lua_tointegerx) (lua_State *L, int idx, int *isnum);
extern int (lua_toboolean) (lua_State *L, int idx);
extern const char *(lua_tolstring) (lua_State *L, int idx, size_t *len);
extern lua_Unsigned (lua_rawlen) (lua_State *L, int idx);
extern lua_CFunction (lua_tocfunction) (lua_State *L, int idx);
extern void *(lua_touserdata) (lua_State *L, int idx);
extern lua_State *(lua_tothread) (lua_State *L, int idx);
extern const void *(lua_topointer) (lua_State *L, int idx);
# 231 "lua.h"
extern void (lua_arith) (lua_State *L, int op);





extern int (lua_rawequal) (lua_State *L, int idx1, int idx2);
extern int (lua_compare) (lua_State *L, int idx1, int idx2, int op);





extern void (lua_pushnil) (lua_State *L);
extern void (lua_pushnumber) (lua_State *L, lua_Number n);
extern void (lua_pushinteger) (lua_State *L, lua_Integer n);
extern const char *(lua_pushlstring) (lua_State *L, const char *s, size_t len);
extern const char *(lua_pushstring) (lua_State *L, const char *s);
extern const char *(lua_pushvfstring) (lua_State *L, const char *fmt,
                                                      va_list argp);
extern const char *(lua_pushfstring) (lua_State *L, const char *fmt, ...);
extern void (lua_pushcclosure) (lua_State *L, lua_CFunction fn, int n);
extern void (lua_pushboolean) (lua_State *L, int b);
extern void (lua_pushlightuserdata) (lua_State *L, void *p);
extern int (lua_pushthread) (lua_State *L);





extern int (lua_getglobal) (lua_State *L, const char *name);
extern int (lua_gettable) (lua_State *L, int idx);
extern int (lua_getfield) (lua_State *L, int idx, const char *k);
extern int (lua_geti) (lua_State *L, int idx, lua_Integer n);
extern int (lua_rawget) (lua_State *L, int idx);
extern int (lua_rawgeti) (lua_State *L, int idx, lua_Integer n);
extern int (lua_rawgetp) (lua_State *L, int idx, const void *p);

extern void (lua_createtable) (lua_State *L, int narr, int nrec);
extern void *(lua_newuserdatauv) (lua_State *L, size_t sz, int nuvalue);
extern int (lua_getmetatable) (lua_State *L, int objindex);
extern int (lua_getiuservalue) (lua_State *L, int idx, int n);





extern void (lua_setglobal) (lua_State *L, const char *name);
extern void (lua_settable) (lua_State *L, int idx);
extern void (lua_setfield) (lua_State *L, int idx, const char *k);
extern void (lua_seti) (lua_State *L, int idx, lua_Integer n);
extern void (lua_rawset) (lua_State *L, int idx);
extern void (lua_rawseti) (lua_State *L, int idx, lua_Integer n);
extern void (lua_rawsetp) (lua_State *L, int idx, const void *p);
extern int (lua_setmetatable) (lua_State *L, int objindex);
extern int (lua_setiuservalue) (lua_State *L, int idx, int n);





extern void (lua_callk) (lua_State *L, int nargs, int nresults,
                           lua_KContext ctx, lua_KFunction k);


extern int (lua_pcallk) (lua_State *L, int nargs, int nresults, int errfunc,
                            lua_KContext ctx, lua_KFunction k);


extern int (lua_load) (lua_State *L, lua_Reader reader, void *dt,
                          const char *chunkname, const char *mode);

extern int (lua_dump) (lua_State *L, lua_Writer writer, void *data, int strip);





extern int (lua_yieldk) (lua_State *L, int nresults, lua_KContext ctx,
                               lua_KFunction k);
extern int (lua_resume) (lua_State *L, lua_State *from, int narg,
                               int *nres);
extern int (lua_status) (lua_State *L);
extern int (lua_isyieldable) (lua_State *L);







extern void (lua_setwarnf) (lua_State *L, lua_WarnFunction f, void *ud);
extern void (lua_warning) (lua_State *L, const char *msg, int tocont);
# 342 "lua.h"
extern int (lua_gc) (lua_State *L, int what, ...);






extern int (lua_error) (lua_State *L);

extern int (lua_next) (lua_State *L, int idx);

extern void (lua_concat) (lua_State *L, int n);
extern void (lua_len) (lua_State *L, int idx);

extern size_t (lua_stringtonumber) (lua_State *L, const char *s);

extern lua_Alloc (lua_getallocf) (lua_State *L, void **ud);
extern void (lua_setallocf) (lua_State *L, lua_Alloc f, void *ud);

extern void (lua_toclose) (lua_State *L, int idx);
extern void (lua_closeslot) (lua_State *L, int idx);
# 457 "lua.h"
extern int (lua_getstack) (lua_State *L, int level, lua_Debug *ar);
extern int (lua_getinfo) (lua_State *L, const char *what, lua_Debug *ar);
extern const char *(lua_getlocal) (lua_State *L, const lua_Debug *ar, int n);
extern const char *(lua_setlocal) (lua_State *L, const lua_Debug *ar, int n);
extern const char *(lua_getupvalue) (lua_State *L, int funcindex, int n);
extern const char *(lua_setupvalue) (lua_State *L, int funcindex, int n);

extern void *(lua_upvalueid) (lua_State *L, int fidx, int n);
extern void (lua_upvaluejoin) (lua_State *L, int fidx1, int n1,
                                               int fidx2, int n2);

extern void (lua_sethook) (lua_State *L, lua_Hook func, int mask, int count);
extern lua_Hook (lua_gethook) (lua_State *L);
extern int (lua_gethookmask) (lua_State *L);
extern int (lua_gethookcount) (lua_State *L);

extern int (lua_setcstacklimit) (lua_State *L, unsigned int limit);

struct lua_Debug {
  int event;
  const char *name;
  const char *namewhat;
  const char *what;
  const char *source;
  size_t srclen;
  int currentline;
  int linedefined;
  int lastlinedefined;
  unsigned char nups;
  unsigned char nparams;
  char isvararg;
  char istailcall;
  unsigned short ftransfer;
  unsigned short ntransfer;
  char short_src[60];

  struct CallInfo *i_ci;
};
# 20 "lvm.c" 2

# 1 "ldebug.h" 1
# 11 "ldebug.h"
# 1 "lstate.h" 1
# 14 "lstate.h"
typedef struct CallInfo CallInfo;


# 1 "lobject.h" 1
# 12 "lobject.h"
# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stdarg.h" 1 3 4
# 1 "C:/msys64/mingw64/include/stdarg.h" 1 3 4
# 2 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stdarg.h" 2 3 4
# 13 "lobject.h" 2


# 1 "llimits.h" 1
# 11 "llimits.h"
# 1 "C:/msys64/mingw64/include/limits.h" 1 3
# 12 "llimits.h" 2
# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 1 3 4
# 1 "C:/msys64/mingw64/include/stddef.h" 1 3 4
# 2 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 2 3 4
# 13 "llimits.h" 2
# 27 "llimits.h"
typedef size_t lu_mem;
typedef ptrdiff_t l_mem;







typedef unsigned char lu_byte;
typedef signed char ls_byte;
# 96 "llimits.h"
typedef double l_uacNumber;
typedef long long l_uacInt;
# 200 "llimits.h"
typedef unsigned int l_uint32;




typedef l_uint32 Instruction;
# 16 "lobject.h" 2
# 49 "lobject.h"
typedef union Value {
  struct GCObject *gc;
  void *p;
  lua_CFunction f;
  lua_Integer i;
  lua_Number n;

  lu_byte ub;
} Value;
# 67 "lobject.h"
typedef struct TValue {
  Value value_; lu_byte tt_;
} TValue;
# 148 "lobject.h"
typedef union StackValue {
  TValue val;
  struct {
    Value value_; lu_byte tt_;
    unsigned short delta;
  } tbclist;
} StackValue;



typedef StackValue *StkId;






typedef union {
  StkId p;
  ptrdiff_t offset;
} StkIdRel;
# 292 "lobject.h"
typedef struct GCObject {
  struct GCObject *next; lu_byte tt; lu_byte marked;
} GCObject;
# 386 "lobject.h"
typedef struct TString {
  struct GCObject *next; lu_byte tt; lu_byte marked;
  lu_byte extra;
  lu_byte shrlen;
  unsigned int hash;
  union {
    size_t lnglen;
    struct TString *hnext;
  } u;
  char contents[1];
} TString;
# 451 "lobject.h"
typedef union UValue {
  TValue uv;
  lua_Number n; double u; void *s; lua_Integer i; long l;
} UValue;






typedef struct Udata {
  struct GCObject *next; lu_byte tt; lu_byte marked;
  unsigned short nuvalue;
  size_t len;
  struct Table *metatable;
  GCObject *gclist;
  UValue uv[1];
} Udata;
# 480 "lobject.h"
typedef struct Udata0 {
  struct GCObject *next; lu_byte tt; lu_byte marked;
  unsigned short nuvalue;
  size_t len;
  struct Table *metatable;
  union {lua_Number n; double u; void *s; lua_Integer i; long l;} bindata;
} Udata0;
# 515 "lobject.h"
typedef struct Upvaldesc {
  TString *name;
  lu_byte instack;
  lu_byte idx;
  lu_byte kind;
} Upvaldesc;






typedef struct LocVar {
  TString *varname;
  int startpc;
  int endpc;
} LocVar;
# 544 "lobject.h"
typedef struct AbsLineInfo {
  int pc;
  int line;
} AbsLineInfo;




typedef struct Proto {
  struct GCObject *next; lu_byte tt; lu_byte marked;
  lu_byte numparams;
  lu_byte is_vararg;
  lu_byte maxstacksize;
  int sizeupvalues;
  int sizek;
  int sizecode;
  int sizelineinfo;
  int sizep;
  int sizelocvars;
  int sizeabslineinfo;
  int linedefined;
  int lastlinedefined;
  TValue *k;
  Instruction *code;
  struct Proto **p;
  Upvaldesc *upvalues;
  ls_byte *lineinfo;
  AbsLineInfo *abslineinfo;
  LocVar *locvars;
  TString *source;
  GCObject *gclist;
} Proto;
# 629 "lobject.h"
typedef struct UpVal {
  struct GCObject *next; lu_byte tt; lu_byte marked;
  union {
    TValue *p;
    ptrdiff_t offset;
  } v;
  union {
    struct {
      struct UpVal *next;
      struct UpVal **previous;
    } open;
    TValue value;
  } u;
} UpVal;






typedef struct CClosure {
  struct GCObject *next; lu_byte tt; lu_byte marked; lu_byte nupvalues; GCObject *gclist;
  lua_CFunction f;
  TValue upvalue[1];
} CClosure;


typedef struct LClosure {
  struct GCObject *next; lu_byte tt; lu_byte marked; lu_byte nupvalues; GCObject *gclist;
  struct Proto *p;
  UpVal *upvals[1];
} LClosure;


typedef union Closure {
  CClosure c;
  LClosure l;
} Closure;
# 701 "lobject.h"
typedef union Node {
  struct NodeKey {
    Value value_; lu_byte tt_;
    lu_byte key_tt;
    int next;
    Value key_val;
  } u;
  TValue i_val;
} Node;
# 739 "lobject.h"
typedef struct Table {
  struct GCObject *next; lu_byte tt; lu_byte marked;
  lu_byte flags;
  lu_byte lsizenode;
  unsigned int alimit;
  TValue *array;
  Node *node;
  Node *lastfree;
  struct Table *metatable;
  GCObject *gclist;
} Table;
# 799 "lobject.h"
extern int luaO_utf8esc (char *buff, unsigned long x);
extern int luaO_ceillog2 (unsigned int x);
extern int luaO_rawarith (lua_State *L, int op, const TValue *p1,
                             const TValue *p2, TValue *res);
extern void luaO_arith (lua_State *L, int op, const TValue *p1,
                           const TValue *p2, StkId res);
extern size_t luaO_str2num (const char *s, TValue *o);
extern int luaO_hexavalue (int c);
extern void luaO_tostring (lua_State *L, TValue *obj);
extern const char *luaO_pushvfstring (lua_State *L, const char *fmt,
                                                       va_list argp);
extern const char *luaO_pushfstring (lua_State *L, const char *fmt, ...);
extern void luaO_chunkid (char *out, const char *source, size_t srclen);
# 18 "lstate.h" 2
# 1 "ltm.h" 1
# 12 "ltm.h"
# 1 "lstate.h" 1
# 13 "ltm.h" 2






typedef enum {
  TM_INDEX,
  TM_NEWINDEX,
  TM_GC,
  TM_MODE,
  TM_LEN,
  TM_EQ,
  TM_ADD,
  TM_SUB,
  TM_MUL,
  TM_MOD,
  TM_POW,
  TM_DIV,
  TM_IDIV,
  TM_BAND,
  TM_BOR,
  TM_BXOR,
  TM_SHL,
  TM_SHR,
  TM_UNM,
  TM_BNOT,
  TM_LT,
  TM_LE,
  TM_CONCAT,
  TM_CALL,
  TM_CLOSE,
  TM_N
} TMS;
# 72 "ltm.h"
extern const char *const luaT_typenames_[((9 +1) + 2)];


extern const char *luaT_objtypename (lua_State *L, const TValue *o);

extern const TValue *luaT_gettm (Table *events, TMS event, TString *ename);
extern const TValue *luaT_gettmbyobj (lua_State *L, const TValue *o,
                                                       TMS event);
extern void luaT_init (lua_State *L);

extern void luaT_callTM (lua_State *L, const TValue *f, const TValue *p1,
                            const TValue *p2, const TValue *p3);
extern void luaT_callTMres (lua_State *L, const TValue *f,
                            const TValue *p1, const TValue *p2, StkId p3);
extern void luaT_trybinTM (lua_State *L, const TValue *p1, const TValue *p2,
                              StkId res, TMS event);
extern void luaT_tryconcatTM (lua_State *L);
extern void luaT_trybinassocTM (lua_State *L, const TValue *p1,
       const TValue *p2, int inv, StkId res, TMS event);
extern void luaT_trybiniTM (lua_State *L, const TValue *p1, lua_Integer i2,
                               int inv, StkId res, TMS event);
extern int luaT_callorderTM (lua_State *L, const TValue *p1,
                                const TValue *p2, TMS event);
extern int luaT_callorderiTM (lua_State *L, const TValue *p1, int v2,
                                 int inv, int isfloat, TMS event);

extern void luaT_adjustvarargs (lua_State *L, int nfixparams,
                                   CallInfo *ci, const Proto *p);
extern void luaT_getvarargs (lua_State *L, CallInfo *ci,
                                              StkId where, int wanted);
# 19 "lstate.h" 2
# 1 "lzio.h" 1
# 13 "lzio.h"
# 1 "lmem.h" 1
# 11 "lmem.h"
# 1 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 1 3 4
# 1 "C:/msys64/mingw64/include/stddef.h" 1 3 4
# 2 "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/12.2.0/include/stddef.h" 2 3 4
# 12 "lmem.h" 2
# 77 "lmem.h"
extern void __attribute__((noreturn)) luaM_toobig (lua_State *L);


extern void *luaM_realloc_ (lua_State *L, void *block, size_t oldsize,
                                                          size_t size);
extern void *luaM_saferealloc_ (lua_State *L, void *block, size_t oldsize,
                                                              size_t size);
extern void luaM_free_ (lua_State *L, void *block, size_t osize);
extern void *luaM_growaux_ (lua_State *L, void *block, int nelems,
                               int *size, int size_elem, int limit,
                               const char *what);
extern void *luaM_shrinkvector_ (lua_State *L, void *block, int *nelem,
                                    int final_n, int size_elem);
extern void *luaM_malloc_ (lua_State *L, size_t size, int tag);
# 14 "lzio.h" 2




typedef struct Zio ZIO;




typedef struct Mbuffer {
  char *buffer;
  size_t n;
  size_t buffsize;
} Mbuffer;
# 47 "lzio.h"
extern void luaZ_init (lua_State *L, ZIO *z, lua_Reader reader,
                                        void *data);
extern size_t luaZ_read (ZIO* z, void *b, size_t n);





struct Zio {
  size_t n;
  const char *p;
  lua_Reader reader;
  void *data;
  lua_State *L;
};


extern int luaZ_fill (ZIO *z);
# 20 "lstate.h" 2
# 122 "lstate.h"
struct lua_longjmp;







# 1 "C:/msys64/mingw64/include/signal.h" 1 3
# 10 "C:/msys64/mingw64/include/signal.h" 3
# 1 "C:/msys64/mingw64/include/pthread_signal.h" 1 3
# 11 "C:/msys64/mingw64/include/signal.h" 2 3







  
# 18 "C:/msys64/mingw64/include/signal.h" 3
 typedef int sig_atomic_t;
# 48 "C:/msys64/mingw64/include/signal.h" 3
  typedef void (*__p_sig_fn_t)(int);
# 57 "C:/msys64/mingw64/include/signal.h" 3
  extern void **__attribute__((__cdecl__)) __pxcptinfoptrs(void);


  __p_sig_fn_t __attribute__((__cdecl__)) signal(int _SigNum,__p_sig_fn_t _Func);
  int __attribute__((__cdecl__)) raise(int _SigNum);
# 131 "lstate.h" 2
# 155 "lstate.h"

# 155 "lstate.h"
typedef struct stringtable {
  TString **hash;
  int nuse;
  int size;
} stringtable;
# 177 "lstate.h"
struct CallInfo {
  StkIdRel func;
  StkIdRel top;
  struct CallInfo *previous, *next;
  union {
    struct {
      const Instruction *savedpc;
      volatile sig_atomic_t trap;
      int nextraargs;
    } l;
    struct {
      lua_KFunction k;
      ptrdiff_t old_errfunc;
      lua_KContext ctx;
    } c;
  } u;
  union {
    int funcidx;
    int nyield;
    int nres;
    struct {
      unsigned short ftransfer;
      unsigned short ntransfer;
    } transferinfo;
  } u2;
  short nresults;
  unsigned short callstatus;
};
# 254 "lstate.h"
typedef struct global_State {
  lua_Alloc frealloc;
  void *ud;
  l_mem totalbytes;
  l_mem GCdebt;
  lu_mem GCestimate;
  lu_mem lastatomic;
  stringtable strt;
  TValue l_registry;
  TValue nilvalue;
  unsigned int seed;
  lu_byte currentwhite;
  lu_byte gcstate;
  lu_byte gckind;
  lu_byte gcstopem;
  lu_byte genminormul;
  lu_byte genmajormul;
  lu_byte gcstp;
  lu_byte gcemergency;
  lu_byte gcpause;
  lu_byte gcstepmul;
  lu_byte gcstepsize;
  GCObject *allgc;
  GCObject **sweepgc;
  GCObject *finobj;
  GCObject *gray;
  GCObject *grayagain;
  GCObject *weak;
  GCObject *ephemeron;
  GCObject *allweak;
  GCObject *tobefnz;
  GCObject *fixedgc;

  GCObject *survival;
  GCObject *old1;
  GCObject *reallyold;
  GCObject *firstold1;
  GCObject *finobjsur;
  GCObject *finobjold1;
  GCObject *finobjrold;
  struct lua_State *twups;
  lua_CFunction panic;
  struct lua_State *mainthread;
  TString *memerrmsg;
  TString *tmname[TM_N];
  struct Table *mt[9];
  TString *strcache[53][2];
  lua_WarnFunction warnf;
  void *ud_warn;
} global_State;





struct lua_State {
  struct GCObject *next; lu_byte tt; lu_byte marked;
  lu_byte status;
  lu_byte allowhook;
  unsigned short nci;
  StkIdRel top;
  global_State *l_G;
  CallInfo *ci;
  StkIdRel stack_last;
  StkIdRel stack;
  UpVal *openupval;
  StkIdRel tbclist;
  GCObject *gclist;
  struct lua_State *twups;
  struct lua_longjmp *errorJmp;
  CallInfo base_ci;
  volatile lua_Hook hook;
  ptrdiff_t errfunc;
  l_uint32 nCcalls;
  int oldpc;
  int basehookcount;
  int hookcount;
  volatile sig_atomic_t hookmask;
};
# 353 "lstate.h"
union GCUnion {
  GCObject gc;
  struct TString ts;
  struct Udata u;
  union Closure cl;
  struct Table h;
  struct Proto p;
  struct lua_State th;
  struct UpVal upv;
};
# 396 "lstate.h"
extern void luaE_setdebt (global_State *g, l_mem debt);
extern void luaE_freethread (lua_State *L, lua_State *L1);
extern CallInfo *luaE_extendCI (lua_State *L);
extern void luaE_freeCI (lua_State *L);
extern void luaE_shrinkCI (lua_State *L);
extern void luaE_checkcstack (lua_State *L);
extern void luaE_incCstack (lua_State *L);
extern void luaE_warning (lua_State *L, const char *msg, int tocont);
extern void luaE_warnerror (lua_State *L, const char *where);
extern int luaE_resetthread (lua_State *L, int status);
# 12 "ldebug.h" 2
# 39 "ldebug.h"
extern int luaG_getfuncline (const Proto *f, int pc);
extern const char *luaG_findlocal (lua_State *L, CallInfo *ci, int n,
                                                    StkId *pos);
extern void __attribute__((noreturn)) luaG_typeerror (lua_State *L, const TValue *o,
                                                const char *opname);
extern void __attribute__((noreturn)) luaG_callerror (lua_State *L, const TValue *o);
extern void __attribute__((noreturn)) luaG_forerror (lua_State *L, const TValue *o,
                                               const char *what);
extern void __attribute__((noreturn)) luaG_concaterror (lua_State *L, const TValue *p1,
                                                  const TValue *p2);
extern void __attribute__((noreturn)) luaG_opinterror (lua_State *L, const TValue *p1,
                                                 const TValue *p2,
                                                 const char *msg);
extern void __attribute__((noreturn)) luaG_tointerror (lua_State *L, const TValue *p1,
                                                 const TValue *p2);
extern void __attribute__((noreturn)) luaG_ordererror (lua_State *L, const TValue *p1,
                                                 const TValue *p2);
extern void __attribute__((noreturn)) luaG_runerror (lua_State *L, const char *fmt, ...);
extern const char *luaG_addinfo (lua_State *L, const char *msg,
                                                  TString *src, int line);
extern void __attribute__((noreturn)) luaG_errormsg (lua_State *L);
extern int luaG_traceexec (lua_State *L, const Instruction *pc);
# 22 "lvm.c" 2
# 1 "ldo.h" 1
# 61 "ldo.h"
typedef void (*Pfunc) (lua_State *L, void *ud);

extern void luaD_seterrorobj (lua_State *L, int errcode, StkId oldtop);
extern int luaD_protectedparser (lua_State *L, ZIO *z, const char *name,
                                                  const char *mode);
extern void luaD_hook (lua_State *L, int event, int line,
                                        int fTransfer, int nTransfer);
extern void luaD_hookcall (lua_State *L, CallInfo *ci);
extern int luaD_pretailcall (lua_State *L, CallInfo *ci, StkId func,
                                              int narg1, int delta);
extern CallInfo *luaD_precall (lua_State *L, StkId func, int nResults);
extern void luaD_call (lua_State *L, StkId func, int nResults);
extern void luaD_callnoyield (lua_State *L, StkId func, int nResults);
extern StkId luaD_tryfuncTM (lua_State *L, StkId func);
extern int luaD_closeprotected (lua_State *L, ptrdiff_t level, int status);
extern int luaD_pcall (lua_State *L, Pfunc func, void *u,
                                        ptrdiff_t oldtop, ptrdiff_t ef);
extern void luaD_poscall (lua_State *L, CallInfo *ci, int nres);
extern int luaD_reallocstack (lua_State *L, int newsize, int raiseerror);
extern int luaD_growstack (lua_State *L, int n, int raiseerror);
extern void luaD_shrinkstack (lua_State *L);
extern void luaD_inctop (lua_State *L);

extern void __attribute__((noreturn)) luaD_throw (lua_State *L, int errcode);
extern int luaD_rawrunprotected (lua_State *L, Pfunc f, void *ud);
# 23 "lvm.c" 2
# 1 "lfunc.h" 1
# 50 "lfunc.h"
extern Proto *luaF_newproto (lua_State *L);
extern CClosure *luaF_newCclosure (lua_State *L, int nupvals);
extern LClosure *luaF_newLclosure (lua_State *L, int nupvals);
extern void luaF_initupvals (lua_State *L, LClosure *cl);
extern UpVal *luaF_findupval (lua_State *L, StkId level);
extern void luaF_newtbcupval (lua_State *L, StkId level);
extern void luaF_closeupval (lua_State *L, StkId level);
extern StkId luaF_close (lua_State *L, StkId level, int status, int yy);
extern void luaF_unlinkupval (UpVal *uv);
extern void luaF_freeproto (lua_State *L, Proto *f);
extern const char *luaF_getlocalname (const Proto *func, int local_number,
                                         int pc);
# 24 "lvm.c" 2
# 1 "lgc.h" 1
# 188 "lgc.h"
extern void luaC_fix (lua_State *L, GCObject *o);
extern void luaC_freeallobjects (lua_State *L);
extern void luaC_step (lua_State *L);
extern void luaC_runtilstate (lua_State *L, int statesmask);
extern void luaC_fullgc (lua_State *L, int isemergency);
extern GCObject *luaC_newobj (lua_State *L, int tt, size_t sz);
extern GCObject *luaC_newobjdt (lua_State *L, int tt, size_t sz,
                                                 size_t offset);
extern void luaC_barrier_ (lua_State *L, GCObject *o, GCObject *v);
extern void luaC_barrierback_ (lua_State *L, GCObject *o);
extern void luaC_checkfinalizer (lua_State *L, GCObject *o, Table *mt);
extern void luaC_changemode (lua_State *L, int newmode);
# 25 "lvm.c" 2

# 1 "lopcodes.h" 1
# 32 "lopcodes.h"
enum OpMode {iABC, iABx, iAsBx, iAx, isJ};
# 197 "lopcodes.h"
typedef enum {



OP_MOVE,
OP_LOADI,
OP_LOADF,
OP_LOADK,
OP_LOADKX,
OP_LOADFALSE,
OP_LFALSESKIP,
OP_LOADTRUE,
OP_LOADNIL,
OP_GETUPVAL,
OP_SETUPVAL,

OP_GETTABUP,
OP_GETTABLE,
OP_GETI,
OP_GETFIELD,

OP_SETTABUP,
OP_SETTABLE,
OP_SETI,
OP_SETFIELD,

OP_NEWTABLE,

OP_SELF,

OP_ADDI,

OP_ADDK,
OP_SUBK,
OP_MULK,
OP_MODK,
OP_POWK,
OP_DIVK,
OP_IDIVK,

OP_BANDK,
OP_BORK,
OP_BXORK,

OP_SHRI,
OP_SHLI,

OP_ADD,
OP_SUB,
OP_MUL,
OP_MOD,
OP_POW,
OP_DIV,
OP_IDIV,

OP_BAND,
OP_BOR,
OP_BXOR,
OP_SHL,
OP_SHR,

OP_MMBIN,
OP_MMBINI,
OP_MMBINK,

OP_UNM,
OP_BNOT,
OP_NOT,
OP_LEN,

OP_CONCAT,

OP_CLOSE,
OP_TBC,
OP_JMP,
OP_EQ,
OP_LT,
OP_LE,

OP_EQK,
OP_EQI,
OP_LTI,
OP_LEI,
OP_GTI,
OP_GEI,

OP_TEST,
OP_TESTSET,

OP_CALL,
OP_TAILCALL,

OP_RETURN,
OP_RETURN0,
OP_RETURN1,

OP_FORLOOP,
OP_FORPREP,


OP_TFORPREP,
OP_TFORCALL,
OP_TFORLOOP,

OP_SETLIST,

OP_CLOSURE,

OP_VARARG,

OP_VARARGPREP,

OP_EXTRAARG
} OpCode;
# 381 "lopcodes.h"
extern const lu_byte luaP_opmodes[((int)(OP_EXTRAARG) + 1)];
# 27 "lvm.c" 2

# 1 "lstring.h" 1
# 44 "lstring.h"
extern unsigned int luaS_hash (const char *str, size_t l, unsigned int seed);
extern unsigned int luaS_hashlongstr (TString *ts);
extern int luaS_eqlngstr (TString *a, TString *b);
extern void luaS_resize (lua_State *L, int newsize);
extern void luaS_clearcache (global_State *g);
extern void luaS_init (lua_State *L);
extern void luaS_remove (lua_State *L, TString *ts);
extern Udata *luaS_newudata (lua_State *L, size_t s, int nuvalue);
extern TString *luaS_newlstr (lua_State *L, const char *str, size_t l);
extern TString *luaS_new (lua_State *L, const char *str);
extern TString *luaS_createlngstrobj (lua_State *L, size_t l);
# 29 "lvm.c" 2
# 1 "ltable.h" 1
# 38 "ltable.h"
extern const TValue *luaH_getint (Table *t, lua_Integer key);
extern void luaH_setint (lua_State *L, Table *t, lua_Integer key,
                                                    TValue *value);
extern const TValue *luaH_getshortstr (Table *t, TString *key);
extern const TValue *luaH_getstr (Table *t, TString *key);
extern const TValue *luaH_get (Table *t, const TValue *key);
extern void luaH_newkey (lua_State *L, Table *t, const TValue *key,
                                                    TValue *value);
extern void luaH_set (lua_State *L, Table *t, const TValue *key,
                                                 TValue *value);
extern void luaH_finishset (lua_State *L, Table *t, const TValue *key,
                                       const TValue *slot, TValue *value);
extern Table *luaH_new (lua_State *L);
extern void luaH_resize (lua_State *L, Table *t, unsigned int nasize,
                                                    unsigned int nhsize);
extern void luaH_resizearray (lua_State *L, Table *t, unsigned int nasize);
extern void luaH_free (lua_State *L, Table *t);
extern int luaH_next (lua_State *L, Table *t, StkId key);
extern lua_Unsigned luaH_getn (Table *t);
extern unsigned int luaH_realasize (const Table *t);
# 30 "lvm.c" 2

# 1 "lvm.h" 1
# 43 "lvm.h"
typedef enum {
  F2Ieq,
  F2Ifloor,
  F2Iceil
} F2Imod;
# 120 "lvm.h"
extern int luaV_equalobj (lua_State *L, const TValue *t1, const TValue *t2);
extern int luaV_lessthan (lua_State *L, const TValue *l, const TValue *r);
extern int luaV_lessequal (lua_State *L, const TValue *l, const TValue *r);
extern int luaV_tonumber_ (const TValue *obj, lua_Number *n);
extern int luaV_tointeger (const TValue *obj, lua_Integer *p, F2Imod mode);
extern int luaV_tointegerns (const TValue *obj, lua_Integer *p,
                                F2Imod mode);
extern int luaV_flttointeger (lua_Number n, lua_Integer *p, F2Imod mode);
extern void luaV_finishget (lua_State *L, const TValue *t, TValue *key,
                               StkId val, const TValue *slot);
extern void luaV_finishset (lua_State *L, const TValue *t, TValue *key,
                               TValue *val, const TValue *slot);
extern void luaV_finishOp (lua_State *L);
extern void luaV_execute (lua_State *L, CallInfo *ci);
extern void luaV_concat (lua_State *L, int total);
extern lua_Integer luaV_idiv (lua_State *L, lua_Integer x, lua_Integer y);
extern lua_Integer luaV_mod (lua_State *L, lua_Integer x, lua_Integer y);
extern lua_Number luaV_modf (lua_State *L, lua_Number x, lua_Number y);
extern lua_Integer luaV_shiftl (lua_Integer x, lua_Integer y);
extern void luaV_objlen (lua_State *L, StkId ra, const TValue *rb);
# 32 "lvm.c" 2
# 90 "lvm.c"
static int l_strton (const TValue *obj, TValue *result) {
  ((void)0);
  if (!(((((((obj))->tt_)) & 0x0F)) == (4)))
    return 0;
  else
    return (luaO_str2num(((((&((((union GCUnion *)((((obj)->value_).gc))))->ts))))->contents), result) == ((((&((((union GCUnion *)((((obj)->value_).gc))))->ts))))->tt == ((4) | ((0) << 4)) ? (((&((((union GCUnion *)((((obj)->value_).gc))))->ts))))->shrlen : (((&((((union GCUnion *)((((obj)->value_).gc))))->ts))))->u.lnglen) + 1);
}






int luaV_tonumber_ (const TValue *obj, lua_Number *n) {
  TValue v;
  if (((((obj))->tt_) == (((3) | ((0) << 4))))) {
    *n = ((lua_Number)(((((obj)->value_).i))));
    return 1;
  }
  else if (l_strton(obj, &v)) {
    *n = ((((((&v))->tt_) == (((3) | ((0) << 4)))) ? ((lua_Number)(((((&v)->value_).i)))) : (((&v)->value_).n)));
    return 1;
  }
  else
    return 0;
}





int luaV_flttointeger (lua_Number n, lua_Integer *p, F2Imod mode) {
  lua_Number f = ((lua_Number)floor(n));
  if (n != f) {
    if (mode == F2Ieq) return 0;
    else if (mode == F2Iceil)
      f += 1;
  }
  return ((f) >= (double)(
# 128 "lvm.c" 3
        (-9223372036854775807ll - 1)
# 128 "lvm.c"
        ) && (f) < -(double)(
# 128 "lvm.c" 3
        (-9223372036854775807ll - 1)
# 128 "lvm.c"
        ) && (*(p) = (long long)(f), 1));
}







int luaV_tointegerns (const TValue *obj, lua_Integer *p, F2Imod mode) {
  if (((((obj))->tt_) == (((3) | ((1) << 4)))))
    return luaV_flttointeger((((obj)->value_).n), p, mode);
  else if (((((obj))->tt_) == (((3) | ((0) << 4))))) {
    *p = (((obj)->value_).i);
    return 1;
  }
  else
    return 0;
}





int luaV_tointeger (const TValue *obj, lua_Integer *p, F2Imod mode) {
  TValue v;
  if (l_strton(obj, &v))
    obj = &v;
  return luaV_tointegerns(obj, p, mode);
}
# 176 "lvm.c"
static int forlimit (lua_State *L, lua_Integer init, const TValue *lim,
                                   lua_Integer *p, lua_Integer step) {
  if (!luaV_tointeger(lim, p, (step < 0 ? F2Iceil : F2Ifloor))) {

    lua_Number flim;
    if (!(((((lim))->tt_) == (((3) | ((1) << 4)))) ? (*(&flim) = (((lim)->value_).n), 1) : luaV_tonumber_(lim,&flim)))
      luaG_forerror(L, lim, "limit");

    if (((0)<(flim))) {
      if (step < 0) return 1;
      *p = 
# 186 "lvm.c" 3
          9223372036854775807ll
# 186 "lvm.c"
                        ;
    }
    else {
      if (step > 0) return 1;
      *p = 
# 190 "lvm.c" 3
          (-9223372036854775807ll - 1)
# 190 "lvm.c"
                        ;
    }
  }
  return (step > 0 ? init > *p : init < *p);
}
# 206 "lvm.c"
static int forprep (lua_State *L, StkId ra) {
  TValue *pinit = (&(ra)->val);
  TValue *plimit = (&(ra + 1)->val);
  TValue *pstep = (&(ra + 2)->val);
  if (((((pinit))->tt_) == (((3) | ((0) << 4)))) && ((((pstep))->tt_) == (((3) | ((0) << 4))))) {
    lua_Integer init = (((pinit)->value_).i);
    lua_Integer step = (((pstep)->value_).i);
    lua_Integer limit;
    if (step == 0)
      luaG_runerror(L, "'for' step is zero");
    { TValue *io=((&(ra + 3)->val)); ((io)->value_).i=(init); ((io)->tt_=(((3) | ((0) << 4)))); };
    if (forlimit(L, init, plimit, &limit, step))
      return 1;
    else {
      lua_Unsigned count;
      if (step > 0) {
        count = ((lua_Unsigned)(limit)) - ((lua_Unsigned)(init));
        if (step != 1)
          count /= ((lua_Unsigned)(step));
      }
      else {
        count = ((lua_Unsigned)(init)) - ((lua_Unsigned)(limit));

        count /= ((lua_Unsigned)(-(step + 1))) + 1u;
      }


      { TValue *io=(plimit); ((io)->value_).i=(((lua_Integer)(count))); ((io)->tt_=(((3) | ((0) << 4)))); };
    }
  }
  else {
    lua_Number init; lua_Number limit; lua_Number step;
    if ((__builtin_expect(((!(((((plimit))->tt_) == (((3) | ((1) << 4)))) ? (*(&limit) = (((plimit)->value_).n), 1) : luaV_tonumber_(plimit,&limit))) != 0), 0)))
      luaG_forerror(L, plimit, "limit");
    if ((__builtin_expect(((!(((((pstep))->tt_) == (((3) | ((1) << 4)))) ? (*(&step) = (((pstep)->value_).n), 1) : luaV_tonumber_(pstep,&step))) != 0), 0)))
      luaG_forerror(L, pstep, "step");
    if ((__builtin_expect(((!(((((pinit))->tt_) == (((3) | ((1) << 4)))) ? (*(&init) = (((pinit)->value_).n), 1) : luaV_tonumber_(pinit,&init))) != 0), 0)))
      luaG_forerror(L, pinit, "initial value");
    if (step == 0)
      luaG_runerror(L, "'for' step is zero");
    if (((0)<(step)) ? ((limit)<(init))
                            : ((init)<(limit)))
      return 1;
    else {

      { TValue *io=(plimit); ((io)->value_).n=(limit); ((io)->tt_=(((3) | ((1) << 4)))); };
      { TValue *io=(pstep); ((io)->value_).n=(step); ((io)->tt_=(((3) | ((1) << 4)))); };
      { TValue *io=((&(ra)->val)); ((io)->value_).n=(init); ((io)->tt_=(((3) | ((1) << 4)))); };
      { TValue *io=((&(ra + 3)->val)); ((io)->value_).n=(init); ((io)->tt_=(((3) | ((1) << 4)))); };
    }
  }
  return 0;
}







static int floatforloop (StkId ra) {
  lua_Number step = ((((&(ra + 2)->val))->value_).n);
  lua_Number limit = ((((&(ra + 1)->val))->value_).n);
  lua_Number idx = ((((&(ra)->val))->value_).n);
  idx = ((idx)+(step));
  if (((0)<(step)) ? ((idx)<=(limit))
                          : ((limit)<=(idx))) {
    { TValue *io=((&(ra)->val)); ((void)0); ((io)->value_).n=(idx); };
    { TValue *io=((&(ra + 3)->val)); ((io)->value_).n=(idx); ((io)->tt_=(((3) | ((1) << 4)))); };
    return 1;
  }
  else
    return 0;
}







void luaV_finishget (lua_State *L, const TValue *t, TValue *key, StkId val,
                      const TValue *slot) {
  int loop;
  const TValue *tm;
  for (loop = 0; loop < 2000; loop++) {
    if (slot == 
# 292 "lvm.c" 3 4
               ((void *)0)
# 292 "lvm.c"
                   ) {
      ((void)0);
      tm = luaT_gettmbyobj(L, t, TM_INDEX);
      if ((__builtin_expect((((((((((tm))->tt_)) & 0x0F)) == (0))) != 0), 0)))
        luaG_typeerror(L, t, "index");

    }
    else {
      ((void)0);
      tm = ((((&((((union GCUnion *)((((t)->value_).gc))))->h)))->metatable) == 
# 301 "lvm.c" 3 4
          ((void *)0) 
# 301 "lvm.c"
          ? 
# 301 "lvm.c" 3 4
          ((void *)0) 
# 301 "lvm.c"
          : ((((&((((union GCUnion *)((((t)->value_).gc))))->h)))->metatable)->flags & (1u<<(TM_INDEX))) ? 
# 301 "lvm.c" 3 4
          ((void *)0) 
# 301 "lvm.c"
          : luaT_gettm(((&((((union GCUnion *)((((t)->value_).gc))))->h)))->metatable, TM_INDEX, ((L->l_G))->tmname[TM_INDEX]));
      if (tm == 
# 302 "lvm.c" 3 4
               ((void *)0)
# 302 "lvm.c"
                   ) {
        (((&(val)->val))->tt_=(((0) | ((0) << 4))));
        return;
      }

    }
    if (((((((tm)->tt_)) & 0x0F)) == (6))) {
      luaT_callTMres(L, tm, t, key, val);
      return;
    }
    t = tm;
    if ((!((((t))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 313 "lvm.c" 3 4
       ((void *)0)
# 313 "lvm.c"
       , 0) : (slot = luaH_get(((&((((union GCUnion *)((((t)->value_).gc))))->h))), key), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
      { TValue *io1=((&(val)->val)); const TValue *io2=(slot); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
      return;
    }

  }
  luaG_runerror(L, "'__index' chain too long; possible loop");
}
# 330 "lvm.c"
void luaV_finishset (lua_State *L, const TValue *t, TValue *key,
                     TValue *val, const TValue *slot) {
  int loop;
  for (loop = 0; loop < 2000; loop++) {
    const TValue *tm;
    if (slot != 
# 335 "lvm.c" 3 4
               ((void *)0)
# 335 "lvm.c"
                   ) {
      Table *h = ((&((((union GCUnion *)((((t)->value_).gc))))->h)));
      ((void)0);
      tm = ((h->metatable) == 
# 338 "lvm.c" 3 4
          ((void *)0) 
# 338 "lvm.c"
          ? 
# 338 "lvm.c" 3 4
          ((void *)0) 
# 338 "lvm.c"
          : ((h->metatable)->flags & (1u<<(TM_NEWINDEX))) ? 
# 338 "lvm.c" 3 4
          ((void *)0) 
# 338 "lvm.c"
          : luaT_gettm(h->metatable, TM_NEWINDEX, ((L->l_G))->tmname[TM_NEWINDEX]));
      if (tm == 
# 339 "lvm.c" 3 4
               ((void *)0)
# 339 "lvm.c"
                   ) {
        luaH_finishset(L, h, key, slot, val);
        ((h)->flags &= ~(~(~0u << (TM_EQ + 1))));
        ( (((val)->tt_) & (1 << 6)) ? ( (((((&(((union GCUnion *)((h)))->gc)))->marked) & ((1<<(5)))) && ((((((val)->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrierback_(L,(&(((union GCUnion *)((h)))->gc))) : ((void)((0)))) : ((void)((0))));
        return;
      }

    }
    else {
      tm = luaT_gettmbyobj(L, t, TM_NEWINDEX);
      if ((__builtin_expect((((((((((tm))->tt_)) & 0x0F)) == (0))) != 0), 0)))
        luaG_typeerror(L, t, "index");
    }

    if (((((((tm)->tt_)) & 0x0F)) == (6))) {
      luaT_callTM(L, tm, t, key, val);
      return;
    }
    t = tm;
    if ((!((((t))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 358 "lvm.c" 3 4
       ((void *)0)
# 358 "lvm.c"
       , 0) : (slot = luaH_get(((&((((union GCUnion *)((((t)->value_).gc))))->h))), key), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
      { { TValue *io1=(((TValue *)(slot))); const TValue *io2=(val); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); }; ( (((val)->tt_) & (1 << 6)) ? ( (((((((t)->value_).gc))->marked) & ((1<<(5)))) && ((((((val)->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrierback_(L,(((t)->value_).gc)) : ((void)((0)))) : ((void)((0)))); };
      return;
    }

  }
  luaG_runerror(L, "'__newindex' chain too long; possible loop");
}
# 375 "lvm.c"
static int l_strcmp (const TString *ls, const TString *rs) {
  const char *l = ((ls)->contents);
  size_t ll = ((ls)->tt == ((4) | ((0) << 4)) ? (ls)->shrlen : (ls)->u.lnglen);
  const char *r = ((rs)->contents);
  size_t lr = ((rs)->tt == ((4) | ((0) << 4)) ? (rs)->shrlen : (rs)->u.lnglen);
  for (;;) {
    int temp = strcoll(l, r);
    if (temp != 0)
      return temp;
    else {
      size_t len = strlen(l);
      if (len == lr)
        return (len == ll) ? 0 : 1;
      else if (len == ll)
        return -1;

      len++;
      l += len; ll -= len; r += len; lr -= len;
    }
  }
}
# 409 "lvm.c"
static __inline__ int LTintfloat (lua_Integer i, lua_Number f) {
  if (((((lua_Unsigned)1 << ((53))) + ((lua_Unsigned)(i))) <= (2 * ((lua_Unsigned)1 << ((53))))))
    return ((((lua_Number)((i))))<(f));
  else {
    lua_Integer fi;
    if (luaV_flttointeger(f, &fi, F2Iceil))
      return i < fi;
    else
      return f > 0;
  }
}






static __inline__ int LEintfloat (lua_Integer i, lua_Number f) {
  if (((((lua_Unsigned)1 << ((53))) + ((lua_Unsigned)(i))) <= (2 * ((lua_Unsigned)1 << ((53))))))
    return ((((lua_Number)((i))))<=(f));
  else {
    lua_Integer fi;
    if (luaV_flttointeger(f, &fi, F2Ifloor))
      return i <= fi;
    else
      return f > 0;
  }
}






static __inline__ int LTfloatint (lua_Number f, lua_Integer i) {
  if (((((lua_Unsigned)1 << ((53))) + ((lua_Unsigned)(i))) <= (2 * ((lua_Unsigned)1 << ((53))))))
    return ((f)<(((lua_Number)((i)))));
  else {
    lua_Integer fi;
    if (luaV_flttointeger(f, &fi, F2Ifloor))
      return fi < i;
    else
      return f < 0;
  }
}






static __inline__ int LEfloatint (lua_Number f, lua_Integer i) {
  if (((((lua_Unsigned)1 << ((53))) + ((lua_Unsigned)(i))) <= (2 * ((lua_Unsigned)1 << ((53))))))
    return ((f)<=(((lua_Number)((i)))));
  else {
    lua_Integer fi;
    if (luaV_flttointeger(f, &fi, F2Iceil))
      return fi <= i;
    else
      return f < 0;
  }
}





static __inline__ int LTnum (const TValue *l, const TValue *r) {
  ((void)0);
  if (((((l))->tt_) == (((3) | ((0) << 4))))) {
    lua_Integer li = (((l)->value_).i);
    if (((((r))->tt_) == (((3) | ((0) << 4)))))
      return li < (((r)->value_).i);
    else
      return LTintfloat(li, (((r)->value_).n));
  }
  else {
    lua_Number lf = (((l)->value_).n);
    if (((((r))->tt_) == (((3) | ((1) << 4)))))
      return ((lf)<((((r)->value_).n)));
    else
      return LTfloatint(lf, (((r)->value_).i));
  }
}





static __inline__ int LEnum (const TValue *l, const TValue *r) {
  ((void)0);
  if (((((l))->tt_) == (((3) | ((0) << 4))))) {
    lua_Integer li = (((l)->value_).i);
    if (((((r))->tt_) == (((3) | ((0) << 4)))))
      return li <= (((r)->value_).i);
    else
      return LEintfloat(li, (((r)->value_).n));
  }
  else {
    lua_Number lf = (((l)->value_).n);
    if (((((r))->tt_) == (((3) | ((1) << 4)))))
      return ((lf)<=((((r)->value_).n)));
    else
      return LEfloatint(lf, (((r)->value_).i));
  }
}





static int lessthanothers (lua_State *L, const TValue *l, const TValue *r) {
  ((void)0);
  if ((((((((l))->tt_)) & 0x0F)) == (4)) && (((((((r))->tt_)) & 0x0F)) == (4)))
    return l_strcmp(((&((((union GCUnion *)((((l)->value_).gc))))->ts))), ((&((((union GCUnion *)((((r)->value_).gc))))->ts)))) < 0;
  else
    return luaT_callorderTM(L, l, r, TM_LT);
}





int luaV_lessthan (lua_State *L, const TValue *l, const TValue *r) {
  if ((((((((l))->tt_)) & 0x0F)) == (3)) && (((((((r))->tt_)) & 0x0F)) == (3)))
    return LTnum(l, r);
  else return lessthanothers(L, l, r);
}





static int lessequalothers (lua_State *L, const TValue *l, const TValue *r) {
  ((void)0);
  if ((((((((l))->tt_)) & 0x0F)) == (4)) && (((((((r))->tt_)) & 0x0F)) == (4)))
    return l_strcmp(((&((((union GCUnion *)((((l)->value_).gc))))->ts))), ((&((((union GCUnion *)((((r)->value_).gc))))->ts)))) <= 0;
  else
    return luaT_callorderTM(L, l, r, TM_LE);
}





int luaV_lessequal (lua_State *L, const TValue *l, const TValue *r) {
  if ((((((((l))->tt_)) & 0x0F)) == (3)) && (((((((r))->tt_)) & 0x0F)) == (3)))
    return LEnum(l, r);
  else return lessequalothers(L, l, r);
}






int luaV_equalobj (lua_State *L, const TValue *t1, const TValue *t2) {
  const TValue *tm;
  if (((((t1)->tt_)) & 0x3F) != ((((t2)->tt_)) & 0x3F)) {
    if ((((((t1)->tt_)) & 0x0F)) != (((((t2)->tt_)) & 0x0F)) || (((((t1)->tt_)) & 0x0F)) != 3)
      return 0;
    else {



      lua_Integer i1, i2;
      return (luaV_tointegerns(t1, &i1, F2Ieq) &&
              luaV_tointegerns(t2, &i2, F2Ieq) &&
              i1 == i2);
    }
  }

  switch (((((t1)->tt_)) & 0x3F)) {
    case ((0) | ((0) << 4)): case ((1) | ((0) << 4)): case ((1) | ((1) << 4)): return 1;
    case ((3) | ((0) << 4)): return ((((t1)->value_).i) == (((t2)->value_).i));
    case ((3) | ((1) << 4)): return (((((t1)->value_).n))==((((t2)->value_).n)));
    case ((2) | ((0) << 4)): return (((t1)->value_).p) == (((t2)->value_).p);
    case ((6) | ((1) << 4)): return (((t1)->value_).f) == (((t2)->value_).f);
    case ((4) | ((0) << 4)): return ((((&((((union GCUnion *)((((t1)->value_).gc))))->ts)))) == (((&((((union GCUnion *)((((t2)->value_).gc))))->ts)))));
    case ((4) | ((1) << 4)): return luaS_eqlngstr(((&((((union GCUnion *)((((t1)->value_).gc))))->ts))), ((&((((union GCUnion *)((((t2)->value_).gc))))->ts))));
    case ((7) | ((0) << 4)): {
      if (((&((((union GCUnion *)((((t1)->value_).gc))))->u))) == ((&((((union GCUnion *)((((t2)->value_).gc))))->u)))) return 1;
      else if (L == 
# 591 "lvm.c" 3 4
                   ((void *)0)
# 591 "lvm.c"
                       ) return 0;
      tm = ((((&((((union GCUnion *)((((t1)->value_).gc))))->u)))->metatable) == 
# 592 "lvm.c" 3 4
          ((void *)0) 
# 592 "lvm.c"
          ? 
# 592 "lvm.c" 3 4
          ((void *)0) 
# 592 "lvm.c"
          : ((((&((((union GCUnion *)((((t1)->value_).gc))))->u)))->metatable)->flags & (1u<<(TM_EQ))) ? 
# 592 "lvm.c" 3 4
          ((void *)0) 
# 592 "lvm.c"
          : luaT_gettm(((&((((union GCUnion *)((((t1)->value_).gc))))->u)))->metatable, TM_EQ, ((L->l_G))->tmname[TM_EQ]));
      if (tm == 
# 593 "lvm.c" 3 4
               ((void *)0)
# 593 "lvm.c"
                   )
        tm = ((((&((((union GCUnion *)((((t2)->value_).gc))))->u)))->metatable) == 
# 594 "lvm.c" 3 4
            ((void *)0) 
# 594 "lvm.c"
            ? 
# 594 "lvm.c" 3 4
            ((void *)0) 
# 594 "lvm.c"
            : ((((&((((union GCUnion *)((((t2)->value_).gc))))->u)))->metatable)->flags & (1u<<(TM_EQ))) ? 
# 594 "lvm.c" 3 4
            ((void *)0) 
# 594 "lvm.c"
            : luaT_gettm(((&((((union GCUnion *)((((t2)->value_).gc))))->u)))->metatable, TM_EQ, ((L->l_G))->tmname[TM_EQ]));
      break;
    }
    case ((5) | ((0) << 4)): {
      if (((&((((union GCUnion *)((((t1)->value_).gc))))->h))) == ((&((((union GCUnion *)((((t2)->value_).gc))))->h)))) return 1;
      else if (L == 
# 599 "lvm.c" 3 4
                   ((void *)0)
# 599 "lvm.c"
                       ) return 0;
      tm = ((((&((((union GCUnion *)((((t1)->value_).gc))))->h)))->metatable) == 
# 600 "lvm.c" 3 4
          ((void *)0) 
# 600 "lvm.c"
          ? 
# 600 "lvm.c" 3 4
          ((void *)0) 
# 600 "lvm.c"
          : ((((&((((union GCUnion *)((((t1)->value_).gc))))->h)))->metatable)->flags & (1u<<(TM_EQ))) ? 
# 600 "lvm.c" 3 4
          ((void *)0) 
# 600 "lvm.c"
          : luaT_gettm(((&((((union GCUnion *)((((t1)->value_).gc))))->h)))->metatable, TM_EQ, ((L->l_G))->tmname[TM_EQ]));
      if (tm == 
# 601 "lvm.c" 3 4
               ((void *)0)
# 601 "lvm.c"
                   )
        tm = ((((&((((union GCUnion *)((((t2)->value_).gc))))->h)))->metatable) == 
# 602 "lvm.c" 3 4
            ((void *)0) 
# 602 "lvm.c"
            ? 
# 602 "lvm.c" 3 4
            ((void *)0) 
# 602 "lvm.c"
            : ((((&((((union GCUnion *)((((t2)->value_).gc))))->h)))->metatable)->flags & (1u<<(TM_EQ))) ? 
# 602 "lvm.c" 3 4
            ((void *)0) 
# 602 "lvm.c"
            : luaT_gettm(((&((((union GCUnion *)((((t2)->value_).gc))))->h)))->metatable, TM_EQ, ((L->l_G))->tmname[TM_EQ]));
      break;
    }
    default:
      return (((t1)->value_).gc) == (((t2)->value_).gc);
  }
  if (tm == 
# 608 "lvm.c" 3 4
           ((void *)0)
# 608 "lvm.c"
               )
    return 0;
  else {
    luaT_callTMres(L, tm, t1, t2, L->top.p);
    return !((((((&(L->top.p)->val)))->tt_) == (((1) | ((0) << 4)))) || ((((((((&(L->top.p)->val)))->tt_)) & 0x0F)) == (0)));
  }
}
# 624 "lvm.c"
static void copy2buff (StkId top, int n, char *buff) {
  size_t tl = 0;
  do {
    size_t l = ((((&((((union GCUnion *)(((((&(top - n)->val))->value_).gc))))->ts))))->tt == ((4) | ((0) << 4)) ? (((&((((union GCUnion *)(((((&(top - n)->val))->value_).gc))))->ts))))->shrlen : (((&((((union GCUnion *)(((((&(top - n)->val))->value_).gc))))->ts))))->u.lnglen);
    memcpy(buff + tl, ((((&((((union GCUnion *)(((((&(top - n)->val))->value_).gc))))->ts))))->contents), l * sizeof(char));
    tl += l;
  } while (--n > 0);
}






void luaV_concat (lua_State *L, int total) {
  if (total == 1)
    return;
  do {
    StkId top = L->top.p;
    int n = 2;
    if (!(((((((((&(top - 2)->val)))->tt_)) & 0x0F)) == (4)) || ((((((((&(top - 2)->val)))->tt_)) & 0x0F)) == (3))) ||
        !(((((((((&(top - 1)->val)))->tt_)) & 0x0F)) == (4)) || (((((((((&(top - 1)->val)))->tt_)) & 0x0F)) == (3)) && (luaO_tostring(L, (&(top - 1)->val)), 1))))
      luaT_tryconcatTM(L);
    else if (((((((&(top - 1)->val)))->tt_) == (((((4) | ((0) << 4))) | (1 << 6)))) && ((&((((union GCUnion *)(((((&(top - 1)->val))->value_).gc))))->ts)))->shrlen == 0))
      ((void)(((((((((((&(top - 2)->val)))->tt_)) & 0x0F)) == (4)) || (((((((((&(top - 2)->val)))->tt_)) & 0x0F)) == (3)) && (luaO_tostring(L, (&(top - 2)->val)), 1))))));
    else if (((((((&(top - 2)->val)))->tt_) == (((((4) | ((0) << 4))) | (1 << 6)))) && ((&((((union GCUnion *)(((((&(top - 2)->val))->value_).gc))))->ts)))->shrlen == 0)) {
      { TValue *io1=((&(top - 2)->val)); const TValue *io2=((&(top - 1)->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
    }
    else {

      size_t tl = ((((&((((union GCUnion *)(((((&(top - 1)->val))->value_).gc))))->ts))))->tt == ((4) | ((0) << 4)) ? (((&((((union GCUnion *)(((((&(top - 1)->val))->value_).gc))))->ts))))->shrlen : (((&((((union GCUnion *)(((((&(top - 1)->val))->value_).gc))))->ts))))->u.lnglen);
      TString *ts;

      for (n = 1; n < total && (((((((((&(top - n - 1)->val)))->tt_)) & 0x0F)) == (4)) || (((((((((&(top - n - 1)->val)))->tt_)) & 0x0F)) == (3)) && (luaO_tostring(L, (&(top - n - 1)->val)), 1))); n++) {
        size_t l = ((((&((((union GCUnion *)(((((&(top - n - 1)->val))->value_).gc))))->ts))))->tt == ((4) | ((0) << 4)) ? (((&((((union GCUnion *)(((((&(top - n - 1)->val))->value_).gc))))->ts))))->shrlen : (((&((((union GCUnion *)(((((&(top - n - 1)->val))->value_).gc))))->ts))))->u.lnglen);
        if ((__builtin_expect(((l >= ((sizeof(size_t) < sizeof(lua_Integer) ? ((size_t)(~(size_t)0)) : (size_t)(
# 659 "lvm.c" 3
           9223372036854775807ll
# 659 "lvm.c"
           ))/sizeof(char)) - tl) != 0), 0))) {
          L->top.p = top - total;
          luaG_runerror(L, "string length overflow");
        }
        tl += l;
      }
      if (tl <= 40) {
        char buff[40];
        copy2buff(top, n, buff);
        ts = luaS_newlstr(L, buff, tl);
      }
      else {
        ts = luaS_createlngstrobj(L, tl);
        copy2buff(top, n, ((ts)->contents));
      }
      { TValue *io = ((&(top - n)->val)); TString *x_ = (ts); ((io)->value_).gc = (&(((union GCUnion *)((x_)))->gc)); ((io)->tt_=(((x_->tt) | (1 << 6)))); ((void)L, ((void)0)); };
    }
    total -= n - 1;
    L->top.p -= n - 1;
  } while (total > 1);
}





void luaV_objlen (lua_State *L, StkId ra, const TValue *rb) {
  const TValue *tm;
  switch (((((rb)->tt_)) & 0x3F)) {
    case ((5) | ((0) << 4)): {
      Table *h = ((&((((union GCUnion *)((((rb)->value_).gc))))->h)));
      tm = ((h->metatable) == 
# 690 "lvm.c" 3 4
          ((void *)0) 
# 690 "lvm.c"
          ? 
# 690 "lvm.c" 3 4
          ((void *)0) 
# 690 "lvm.c"
          : ((h->metatable)->flags & (1u<<(TM_LEN))) ? 
# 690 "lvm.c" 3 4
          ((void *)0) 
# 690 "lvm.c"
          : luaT_gettm(h->metatable, TM_LEN, ((L->l_G))->tmname[TM_LEN]));
      if (tm) break;
      { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaH_getn(h)); ((io)->tt_=(((3) | ((0) << 4)))); };
      return;
    }
    case ((4) | ((0) << 4)): {
      { TValue *io=((&(ra)->val)); ((io)->value_).i=(((&((((union GCUnion *)((((rb)->value_).gc))))->ts)))->shrlen); ((io)->tt_=(((3) | ((0) << 4)))); };
      return;
    }
    case ((4) | ((1) << 4)): {
      { TValue *io=((&(ra)->val)); ((io)->value_).i=(((&((((union GCUnion *)((((rb)->value_).gc))))->ts)))->u.lnglen); ((io)->tt_=(((3) | ((0) << 4)))); };
      return;
    }
    default: {
      tm = luaT_gettmbyobj(L, rb, TM_LEN);
      if ((__builtin_expect((((((((((tm))->tt_)) & 0x0F)) == (0))) != 0), 0)))
        luaG_typeerror(L, rb, "get length of");
      break;
    }
  }
  luaT_callTMres(L, tm, rb, rb, ra);
}
# 720 "lvm.c"
lua_Integer luaV_idiv (lua_State *L, lua_Integer m, lua_Integer n) {
  if ((__builtin_expect(((((lua_Unsigned)(n)) + 1u <= 1u) != 0), 0))) {
    if (n == 0)
      luaG_runerror(L, "attempt to divide by zero");
    return ((lua_Integer)(((lua_Unsigned)(0)) - ((lua_Unsigned)(m))));
  }
  else {
    lua_Integer q = m / n;
    if ((m ^ n) < 0 && m % n != 0)
      q -= 1;
    return q;
  }
}







lua_Integer luaV_mod (lua_State *L, lua_Integer m, lua_Integer n) {
  if ((__builtin_expect(((((lua_Unsigned)(n)) + 1u <= 1u) != 0), 0))) {
    if (n == 0)
      luaG_runerror(L, "attempt to perform 'n%%0'");
    return 0;
  }
  else {
    lua_Integer r = m % n;
    if (r != 0 && (r ^ n) < 0)
      r += n;
    return r;
  }
}





lua_Number luaV_modf (lua_State *L, lua_Number m, lua_Number n) {
  lua_Number r;
  { (void)L; (r) = (lua_Number)fmod(m,n); if (((r) > 0) ? (n) < 0 : ((r) < 0 && (n) > 0)) (r) += (n); };
  return r;
}
# 772 "lvm.c"
lua_Integer luaV_shiftl (lua_Integer x, lua_Integer y) {
  if (y < 0) {
    if (y <= -((int)((sizeof(lua_Integer) * 
# 774 "lvm.c" 3
             8
# 774 "lvm.c"
             )))) return 0;
    else return ((lua_Integer)(((lua_Unsigned)(x)) >> ((lua_Unsigned)(-y))));
  }
  else {
    if (y >= ((int)((sizeof(lua_Integer) * 
# 778 "lvm.c" 3
            8
# 778 "lvm.c"
            )))) return 0;
    else return ((lua_Integer)(((lua_Unsigned)(x)) << ((lua_Unsigned)(y))));
  }
}






static void pushclosure (lua_State *L, Proto *p, UpVal **encup, StkId base,
                         StkId ra) {
  int nup = p->sizeupvalues;
  Upvaldesc *uv = p->upvalues;
  int i;
  LClosure *ncl = luaF_newLclosure(L, nup);
  ncl->p = p;
  { TValue *io = ((&(ra)->val)); LClosure *x_ = (ncl); ((io)->value_).gc = (&(((union GCUnion *)((x_)))->gc)); ((io)->tt_=(((((6) | ((0) << 4))) | (1 << 6)))); ((void)L, ((void)0)); };
  for (i = 0; i < nup; i++) {
    if (uv[i].instack)
      ncl->upvals[i] = luaF_findupval(L, base + uv[i].idx);
    else
      ncl->upvals[i] = encup[uv[i].idx];
    ( ((((ncl)->marked) & ((1<<(5)))) && (((ncl->upvals[i])->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrier_(L,(&(((union GCUnion *)((ncl)))->gc)),(&(((union GCUnion *)((ncl->upvals[i])))->gc))) : ((void)((0))));
  }
}





void luaV_finishOp (lua_State *L) {
  CallInfo *ci = L->ci;
  StkId base = ci->func.p + 1;
  Instruction inst = *(ci->u.l.savedpc - 1);
  OpCode op = (((OpCode)(((inst)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))));
  switch (op) {
    case OP_MMBIN: case OP_MMBINI: case OP_MMBINK: {
      { TValue *io1=((&(base + (((int)((((*(ci->u.l.savedpc - 2))>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))->val)); const TValue *io2=((&(--L->top.p)->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
      break;
    }
    case OP_UNM: case OP_BNOT: case OP_LEN:
    case OP_GETTABUP: case OP_GETTABLE: case OP_GETI:
    case OP_GETFIELD: case OP_SELF: {
      { TValue *io1=((&(base + (((int)((((inst)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))->val)); const TValue *io2=((&(--L->top.p)->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
      break;
    }
    case OP_LT: case OP_LE:
    case OP_LTI: case OP_LEI:
    case OP_GTI: case OP_GEI:
    case OP_EQ: {
      int res = !((((((&(L->top.p - 1)->val)))->tt_) == (((1) | ((0) << 4)))) || ((((((((&(L->top.p - 1)->val)))->tt_)) & 0x0F)) == (0)));
      L->top.p--;






      ((void)0);
      if (res != ((((int)((((inst)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0))))))))
        ci->u.l.savedpc++;
      break;
    }
    case OP_CONCAT: {
      StkId top = L->top.p - 1;
      int a = (((int)((((inst)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))));
      int total = ((int)((top - 1 - (base + a))));
      { TValue *io1=((&(top - 2)->val)); const TValue *io2=((&(top)->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
      L->top.p = top - 1;
      luaV_concat(L, total);
      break;
    }
    case OP_CLOSE: {
      ci->u.l.savedpc--;
      break;
    }
    case OP_RETURN: {
      StkId ra = base + (((int)((((inst)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))));


      L->top.p = ra + ci->u2.nres;

      ci->u.l.savedpc--;
      break;
    }
    default: {

      ((void)0)

                                              ;
      break;
    }
  }
}
# 1146 "lvm.c"
void luaV_execute (lua_State *L, CallInfo *ci) {
  LClosure *cl;
  TValue *k;
  StkId base;
  const Instruction *pc;
  int trap;

# 1 "ljumptab.h" 1
# 19 "ljumptab.h"
static const void *const disptab[((int)(OP_EXTRAARG) + 1)] = {
# 28 "ljumptab.h"
&&L_OP_MOVE,
&&L_OP_LOADI,
&&L_OP_LOADF,
&&L_OP_LOADK,
&&L_OP_LOADKX,
&&L_OP_LOADFALSE,
&&L_OP_LFALSESKIP,
&&L_OP_LOADTRUE,
&&L_OP_LOADNIL,
&&L_OP_GETUPVAL,
&&L_OP_SETUPVAL,
&&L_OP_GETTABUP,
&&L_OP_GETTABLE,
&&L_OP_GETI,
&&L_OP_GETFIELD,
&&L_OP_SETTABUP,
&&L_OP_SETTABLE,
&&L_OP_SETI,
&&L_OP_SETFIELD,
&&L_OP_NEWTABLE,
&&L_OP_SELF,
&&L_OP_ADDI,
&&L_OP_ADDK,
&&L_OP_SUBK,
&&L_OP_MULK,
&&L_OP_MODK,
&&L_OP_POWK,
&&L_OP_DIVK,
&&L_OP_IDIVK,
&&L_OP_BANDK,
&&L_OP_BORK,
&&L_OP_BXORK,
&&L_OP_SHRI,
&&L_OP_SHLI,
&&L_OP_ADD,
&&L_OP_SUB,
&&L_OP_MUL,
&&L_OP_MOD,
&&L_OP_POW,
&&L_OP_DIV,
&&L_OP_IDIV,
&&L_OP_BAND,
&&L_OP_BOR,
&&L_OP_BXOR,
&&L_OP_SHL,
&&L_OP_SHR,
&&L_OP_MMBIN,
&&L_OP_MMBINI,
&&L_OP_MMBINK,
&&L_OP_UNM,
&&L_OP_BNOT,
&&L_OP_NOT,
&&L_OP_LEN,
&&L_OP_CONCAT,
&&L_OP_CLOSE,
&&L_OP_TBC,
&&L_OP_JMP,
&&L_OP_EQ,
&&L_OP_LT,
&&L_OP_LE,
&&L_OP_EQK,
&&L_OP_EQI,
&&L_OP_LTI,
&&L_OP_LEI,
&&L_OP_GTI,
&&L_OP_GEI,
&&L_OP_TEST,
&&L_OP_TESTSET,
&&L_OP_CALL,
&&L_OP_TAILCALL,
&&L_OP_RETURN,
&&L_OP_RETURN0,
&&L_OP_RETURN1,
&&L_OP_FORLOOP,
&&L_OP_FORPREP,
&&L_OP_TFORPREP,
&&L_OP_TFORCALL,
&&L_OP_TFORLOOP,
&&L_OP_SETLIST,
&&L_OP_CLOSURE,
&&L_OP_VARARG,
&&L_OP_VARARGPREP,
&&L_OP_EXTRAARG

};
# 1154 "lvm.c" 2

 startfunc:
  trap = L->hookmask;
 returning:
  cl = ((&((((union GCUnion *)(((((&(ci->func.p)->val))->value_).gc))))->cl.l)));
  k = cl->p->k;
  pc = ci->u.l.savedpc;
  if ((__builtin_expect(((trap) != 0), 0))) {
    if (pc == cl->p->code) {
      if (cl->p->is_vararg)
        trap = 0;
      else
        luaD_hookcall(L, ci);
    }
    ci->u.l.trap = 1;
  }
  base = ci->func.p + 1;

  for (;;) {
    Instruction i;
    { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); };




    ((void)0);
    ((void)0);

    ((void)0);
    goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))]; {
      L_OP_MOVE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        { TValue *io1=((&(ra)->val)); const TValue *io2=((&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LOADI: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        lua_Integer b = ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))) - (((1<<(8 + 8 + 1))-1)>>1));
        { TValue *io=((&(ra)->val)); ((io)->value_).i=(b); ((io)->tt_=(((3) | ((0) << 4)))); };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LOADF: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int b = ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))) - (((1<<(8 + 8 + 1))-1)>>1));
        { TValue *io=((&(ra)->val)); ((io)->value_).n=(((lua_Number)((b)))); ((io)->tt_=(((3) | ((1) << 4)))); };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LOADK: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = k + ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))));
        { TValue *io1=((&(ra)->val)); const TValue *io2=(rb); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LOADKX: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb;
        rb = k + ((((int)((((*pc)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0))))))); pc++;
        { TValue *io1=((&(ra)->val)); const TValue *io2=(rb); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LOADFALSE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        (((&(ra)->val))->tt_=(((1) | ((0) << 4))));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LFALSESKIP: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        (((&(ra)->val))->tt_=(((1) | ((0) << 4))));
        pc++;
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LOADTRUE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        (((&(ra)->val))->tt_=(((1) | ((1) << 4))));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LOADNIL: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int b = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        do {
          (((&(ra++)->val))->tt_=(((0) | ((0) << 4))));
        } while (b--);
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_GETUPVAL: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int b = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        { TValue *io1=((&(ra)->val)); const TValue *io2=(cl->upvals[b]->v.p); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SETUPVAL: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        UpVal *uv = cl->upvals[((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))];
        { TValue *io1=(uv->v.p); const TValue *io2=((&(ra)->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        ( ((((&(ra)->val))->tt_) & (1 << 6)) ? ( ((((uv)->marked) & ((1<<(5)))) && (((((((&(ra)->val))->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrier_(L,(&(((union GCUnion *)((uv)))->gc)),(&(((union GCUnion *)((((((&(ra)->val))->value_).gc))))->gc))) : ((void)((0)))) : ((void)((0))));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_GETTABUP: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        TValue *upval = cl->upvals[((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))]->v.p;
        TValue *rc = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))));
        TString *key = ((&((((union GCUnion *)((((rc)->value_).gc))))->ts)));
        if ((!((((upval))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1257 "lvm.c" 3 4
           ((void *)0)
# 1257 "lvm.c"
           , 0) : (slot = luaH_getshortstr(((&((((union GCUnion *)((((upval)->value_).gc))))->h))), key), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { TValue *io1=((&(ra)->val)); const TValue *io2=(slot); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishget(L, upval, rc, ra, slot)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_GETTABLE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        TValue *rc = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        lua_Unsigned n;
        if (((((rc))->tt_) == (((3) | ((0) << 4))))
            ? (((void)((n = (((rc)->value_).i)))), (!((((rb))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1271 "lvm.c" 3 4
                                         ((void *)0)
# 1271 "lvm.c"
                                         , 0) : (slot = (((lua_Unsigned)(n)) - 1u < ((&((((union GCUnion *)((((rb)->value_).gc))))->h)))->alimit) ? &((&((((union GCUnion *)((((rb)->value_).gc))))->h)))->array[n - 1] : luaH_getint(((&((((union GCUnion *)((((rb)->value_).gc))))->h))), n), !(((((((slot))->tt_)) & 0x0F)) == (0)))))
            : (!((((rb))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1272 "lvm.c" 3 4
             ((void *)0)
# 1272 "lvm.c"
             , 0) : (slot = luaH_get(((&((((union GCUnion *)((((rb)->value_).gc))))->h))), rc), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { TValue *io1=((&(ra)->val)); const TValue *io2=(slot); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishget(L, rb, rc, ra, slot)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_GETI: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        int c = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        if ((!((((rb))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1284 "lvm.c" 3 4
           ((void *)0)
# 1284 "lvm.c"
           , 0) : (slot = (((lua_Unsigned)(c)) - 1u < ((&((((union GCUnion *)((((rb)->value_).gc))))->h)))->alimit) ? &((&((((union GCUnion *)((((rb)->value_).gc))))->h)))->array[c - 1] : luaH_getint(((&((((union GCUnion *)((((rb)->value_).gc))))->h))), c), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { TValue *io1=((&(ra)->val)); const TValue *io2=(slot); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        }
        else {
          TValue key;
          { TValue *io=(&key); ((io)->value_).i=(c); ((io)->tt_=(((3) | ((0) << 4)))); };
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishget(L, rb, &key, ra, slot)), (trap = ci->u.l.trap));
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_GETFIELD: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        TValue *rc = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))));
        TString *key = ((&((((union GCUnion *)((((rc)->value_).gc))))->ts)));
        if ((!((((rb))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1300 "lvm.c" 3 4
           ((void *)0)
# 1300 "lvm.c"
           , 0) : (slot = luaH_getshortstr(((&((((union GCUnion *)((((rb)->value_).gc))))->h))), key), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { TValue *io1=((&(ra)->val)); const TValue *io2=(slot); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishget(L, rb, rc, ra, slot)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SETTABUP: {
        const TValue *slot;
        TValue *upval = cl->upvals[(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))]->v.p;
        TValue *rb = (k+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0))))))));
        TValue *rc = ((((((int)((((i) & (1u << ((0 + 7) + 8))))))))) ? k + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) : (&(base + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))))->val));
        TString *key = ((&((((union GCUnion *)((((rb)->value_).gc))))->ts)));
        if ((!((((upval))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1313 "lvm.c" 3 4
           ((void *)0)
# 1313 "lvm.c"
           , 0) : (slot = luaH_getshortstr(((&((((union GCUnion *)((((upval)->value_).gc))))->h))), key), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { { TValue *io1=(((TValue *)(slot))); const TValue *io2=(rc); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); }; ( (((rc)->tt_) & (1 << 6)) ? ( (((((((upval)->value_).gc))->marked) & ((1<<(5)))) && ((((((rc)->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrierback_(L,(((upval)->value_).gc)) : ((void)((0)))) : ((void)((0)))); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishset(L, upval, rb, rc, slot)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SETTABLE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        TValue *rc = ((((((int)((((i) & (1u << ((0 + 7) + 8))))))))) ? k + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) : (&(base + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))))->val));
        lua_Unsigned n;
        if (((((rb))->tt_) == (((3) | ((0) << 4))))
            ? (((void)((n = (((rb)->value_).i)))), (!(((((&(ra)->val)))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1327 "lvm.c" 3 4
                                         ((void *)0)
# 1327 "lvm.c"
                                         , 0) : (slot = (((lua_Unsigned)(n)) - 1u < ((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h)))->alimit) ? &((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h)))->array[n - 1] : luaH_getint(((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h))), n), !(((((((slot))->tt_)) & 0x0F)) == (0)))))
            : (!(((((&(ra)->val)))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1328 "lvm.c" 3 4
             ((void *)0)
# 1328 "lvm.c"
             , 0) : (slot = luaH_get(((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h))), rb), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { { TValue *io1=(((TValue *)(slot))); const TValue *io2=(rc); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); }; ( (((rc)->tt_) & (1 << 6)) ? ( ((((((((&(ra)->val))->value_).gc))->marked) & ((1<<(5)))) && ((((((rc)->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrierback_(L,((((&(ra)->val))->value_).gc)) : ((void)((0)))) : ((void)((0)))); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishset(L, (&(ra)->val), rb, rc, slot)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SETI: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        int c = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rc = ((((((int)((((i) & (1u << ((0 + 7) + 8))))))))) ? k + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) : (&(base + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))))->val));
        if ((!(((((&(ra)->val)))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1340 "lvm.c" 3 4
           ((void *)0)
# 1340 "lvm.c"
           , 0) : (slot = (((lua_Unsigned)(c)) - 1u < ((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h)))->alimit) ? &((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h)))->array[c - 1] : luaH_getint(((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h))), c), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { { TValue *io1=(((TValue *)(slot))); const TValue *io2=(rc); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); }; ( (((rc)->tt_) & (1 << 6)) ? ( ((((((((&(ra)->val))->value_).gc))->marked) & ((1<<(5)))) && ((((((rc)->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrierback_(L,((((&(ra)->val))->value_).gc)) : ((void)((0)))) : ((void)((0)))); };
        }
        else {
          TValue key;
          { TValue *io=(&key); ((io)->value_).i=(c); ((io)->tt_=(((3) | ((0) << 4)))); };
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishset(L, (&(ra)->val), &key, rc, slot)), (trap = ci->u.l.trap));
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SETFIELD: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        TValue *rb = (k+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0))))))));
        TValue *rc = ((((((int)((((i) & (1u << ((0 + 7) + 8))))))))) ? k + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) : (&(base + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))))->val));
        TString *key = ((&((((union GCUnion *)((((rb)->value_).gc))))->ts)));
        if ((!(((((&(ra)->val)))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1356 "lvm.c" 3 4
           ((void *)0)
# 1356 "lvm.c"
           , 0) : (slot = luaH_getshortstr(((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h))), key), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { { TValue *io1=(((TValue *)(slot))); const TValue *io2=(rc); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); }; ( (((rc)->tt_) & (1 << 6)) ? ( ((((((((&(ra)->val))->value_).gc))->marked) & ((1<<(5)))) && ((((((rc)->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrierback_(L,((((&(ra)->val))->value_).gc)) : ((void)((0)))) : ((void)((0)))); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishset(L, (&(ra)->val), rb, rc, slot)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_NEWTABLE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int b = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int c = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        Table *t;
        if (b > 0)
          b = 1 << (b - 1);
        ((void)0);
        if (((((int)((((i) & (1u << ((0 + 7) + 8)))))))))
          c += ((((int)((((*pc)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0))))))) * (((1<<8)-1) + 1);
        pc++;
        L->top.p = ra + 1;
        t = luaH_new(L);
        { TValue *io = ((&(ra)->val)); Table *x_ = (t); ((io)->value_).gc = (&(((union GCUnion *)((x_)))->gc)); ((io)->tt_=(((((5) | ((0) << 4))) | (1 << 6)))); ((void)L, ((void)0)); };
        if (b != 0 || c != 0)
          luaH_resize(L, t, c, b);
        { { if ((L->l_G)->GCdebt > 0) { ((ci->u.l.savedpc = pc), L->top.p = (ra + 1)); luaC_step(L); (trap = ci->u.l.trap);}; ((void)0); }; {((void) 0); ((void) 0);}; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SELF: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        const TValue *slot;
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        TValue *rc = ((((((int)((((i) & (1u << ((0 + 7) + 8))))))))) ? k + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) : (&(base + ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))))->val));
        TString *key = ((&((((union GCUnion *)((((rc)->value_).gc))))->ts)));
        { TValue *io1=((&(ra + 1)->val)); const TValue *io2=(rb); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        if ((!((((rb))->tt_) == (((((5) | ((0) << 4))) | (1 << 6)))) ? (slot = 
# 1389 "lvm.c" 3 4
           ((void *)0)
# 1389 "lvm.c"
           , 0) : (slot = luaH_getstr(((&((((union GCUnion *)((((rb)->value_).gc))))->h))), key), !(((((((slot))->tt_)) & 0x0F)) == (0))))) {
          { TValue *io1=((&(ra)->val)); const TValue *io2=(slot); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_finishget(L, rb, rc, ra, slot)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_ADDI: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); int imm = ((((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1)); if (((((v1))->tt_) == (((3) | ((0) << 4))))) { lua_Integer iv1 = (((v1)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(iv1)) + ((lua_Unsigned)(imm))))); ((io)->tt_=(((3) | ((0) << 4)))); }; } else if (((((v1))->tt_) == (((3) | ((1) << 4))))) { lua_Number nb = (((v1)->value_).n); lua_Number fimm = ((lua_Number)((imm))); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((nb)+(fimm))); ((io)->tt_=(((3) | ((1) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_ADDK: {
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); ((void)0); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) + ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)+(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SUBK: {
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); ((void)0); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) - ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)-(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_MULK: {
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); ((void)0); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) * ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)*(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_MODK: {
        ((ci->u.l.savedpc = pc), L->top.p = ci->top.p);
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); ((void)0); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_mod(L, i1, i2)); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(luaV_modf(L, n1, n2)); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_POWK: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); ((void)0); { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((void)L, (n2 == 2) ? (n1)*(n1) : (lua_Number)pow(n1,n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_DIVK: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); ((void)0); { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)/(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_IDIVK: {
        ((ci->u.l.savedpc = pc), L->top.p = ci->top.p);
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); ((void)0); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_idiv(L, i1, i2)); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((void)L, ((lua_Number)floor(((n1)/(n2)))))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_BANDK: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); lua_Integer i1; lua_Integer i2 = (((v2)->value_).i); if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) & ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_BORK: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); lua_Integer i1; lua_Integer i2 = (((v2)->value_).i); if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) | ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_BXORK: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (k+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))); lua_Integer i1; lua_Integer i2 = (((v2)->value_).i); if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) ^ ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SHRI: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        int ic = ((((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1));
        lua_Integer ib;
        if (((__builtin_expect(((((((rb))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&ib) = (((rb)->value_).i), 1) : luaV_tointegerns(rb,&ib,F2Ieq))) {
          pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_shiftl(ib, -ic)); ((io)->tt_=(((3) | ((0) << 4)))); };
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SHLI: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        int ic = ((((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1));
        lua_Integer ib;
        if (((__builtin_expect(((((((rb))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&ib) = (((rb)->value_).i), 1) : luaV_tointegerns(rb,&ib,F2Ieq))) {
          pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_shiftl(ic, ib)); ((io)->tt_=(((3) | ((0) << 4)))); };
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_ADD: {
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) + ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)+(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SUB: {
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) - ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)-(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_MUL: {
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) * ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)*(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_MOD: {
        ((ci->u.l.savedpc = pc), L->top.p = ci->top.p);
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_mod(L, i1, i2)); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(luaV_modf(L, n1, n2)); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_POW: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((void)L, (n2 == 2) ? (n1)*(n1) : (lua_Number)pow(n1,n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_DIV: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((n1)/(n2))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_IDIV: {
        ((ci->u.l.savedpc = pc), L->top.p = ci->top.p);
        { TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); if (((((v1))->tt_) == (((3) | ((0) << 4)))) && ((((v2))->tt_) == (((3) | ((0) << 4))))) { lua_Integer i1 = (((v1)->value_).i); lua_Integer i2 = (((v2)->value_).i); pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_idiv(L, i1, i2)); ((io)->tt_=(((3) | ((0) << 4)))); }; } else { lua_Number n1; lua_Number n2; if ((((((v1))->tt_) == (((3) | ((1) << 4)))) ? ((n1) = (((v1)->value_).n), 1) : (((((v1))->tt_) == (((3) | ((0) << 4)))) ? ((n1) = ((lua_Number)(((((v1)->value_).i)))), 1) : 0)) && (((((v2))->tt_) == (((3) | ((1) << 4)))) ? ((n2) = (((v2)->value_).n), 1) : (((((v2))->tt_) == (((3) | ((0) << 4)))) ? ((n2) = ((lua_Number)(((((v2)->value_).i)))), 1) : 0))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).n=(((void)L, ((lua_Number)floor(((n1)/(n2)))))); ((io)->tt_=(((3) | ((1) << 4)))); }; }}; }; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_BAND: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); lua_Integer i1; lua_Integer i2; if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq)) && ((__builtin_expect(((((((v2))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i2) = (((v2)->value_).i), 1) : luaV_tointegerns(v2,&i2,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) & ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_BOR: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); lua_Integer i1; lua_Integer i2; if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq)) && ((__builtin_expect(((((((v2))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i2) = (((v2)->value_).i), 1) : luaV_tointegerns(v2,&i2,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) | ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_BXOR: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); lua_Integer i1; lua_Integer i2; if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq)) && ((__builtin_expect(((((((v2))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i2) = (((v2)->value_).i), 1) : luaV_tointegerns(v2,&i2,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(i1)) ^ ((lua_Unsigned)(i2))))); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SHR: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); lua_Integer i1; lua_Integer i2; if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq)) && ((__builtin_expect(((((((v2))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i2) = (((v2)->value_).i), 1) : luaV_tointegerns(v2,&i2,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_shiftl(i1,((lua_Integer)(((lua_Unsigned)(0)) - ((lua_Unsigned)(i2)))))); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_SHL: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); TValue *v1 = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); TValue *v2 = (&((base+((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); lua_Integer i1; lua_Integer i2; if (((__builtin_expect(((((((v1))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i1) = (((v1)->value_).i), 1) : luaV_tointegerns(v1,&i1,F2Ieq)) && ((__builtin_expect(((((((v2))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&i2) = (((v2)->value_).i), 1) : luaV_tointegerns(v2,&i2,F2Ieq))) { pc++; { TValue *io=((&(ra)->val)); ((io)->value_).i=(luaV_shiftl(i1, i2)); ((io)->tt_=(((3) | ((0) << 4)))); }; }};
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_MMBIN: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        Instruction pi = *(pc - 2);
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        TMS tm = (TMS)((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        StkId result = (base+(((int)((((pi)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        ((void)0);
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaT_trybinTM(L, (&(ra)->val), rb, result, tm)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_MMBINI: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        Instruction pi = *(pc - 2);
        int imm = ((((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1));
        TMS tm = (TMS)((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int flip = ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))));
        StkId result = (base+(((int)((((pi)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaT_trybiniTM(L, (&(ra)->val), imm, flip, result, tm)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_MMBINK: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        Instruction pi = *(pc - 2);
        TValue *imm = (k+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0))))))));
        TMS tm = (TMS)((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int flip = ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))));
        StkId result = (base+(((int)((((pi)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaT_trybinassocTM(L, (&(ra)->val), imm, flip, result, tm)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_UNM: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        lua_Number nb;
        if (((((rb))->tt_) == (((3) | ((0) << 4))))) {
          lua_Integer ib = (((rb)->value_).i);
          { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(0)) - ((lua_Unsigned)(ib))))); ((io)->tt_=(((3) | ((0) << 4)))); };
        }
        else if ((((((rb))->tt_) == (((3) | ((1) << 4)))) ? ((nb) = (((rb)->value_).n), 1) : (((((rb))->tt_) == (((3) | ((0) << 4)))) ? ((nb) = ((lua_Number)(((((rb)->value_).i)))), 1) : 0))) {
          { TValue *io=((&(ra)->val)); ((io)->value_).n=((-(nb))); ((io)->tt_=(((3) | ((1) << 4)))); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaT_trybinTM(L, rb, rb, ra, TM_UNM)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_BNOT: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        lua_Integer ib;
        if (((__builtin_expect(((((((rb))->tt_) == (((3) | ((0) << 4))))) != 0), 1)) ? (*(&ib) = (((rb)->value_).i), 1) : luaV_tointegerns(rb,&ib,F2Ieq))) {
          { TValue *io=((&(ra)->val)); ((io)->value_).i=(((lua_Integer)(((lua_Unsigned)(~((lua_Unsigned)(0)))) ^ ((lua_Unsigned)(ib))))); ((io)->tt_=(((3) | ((0) << 4)))); };
        }
        else
          (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaT_trybinTM(L, rb, rb, ra, TM_BNOT)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_NOT: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        if ((((((rb))->tt_) == (((1) | ((0) << 4)))) || (((((((rb))->tt_)) & 0x0F)) == (0))))
          (((&(ra)->val))->tt_=(((1) | ((1) << 4))));
        else
          (((&(ra)->val))->tt_=(((1) | ((0) << 4))));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LEN: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaV_objlen(L, ra, (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val))), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_CONCAT: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int n = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        L->top.p = ra + n;
        ((ci->u.l.savedpc = pc), (luaV_concat(L, n)), (trap = ci->u.l.trap));
        { { if ((L->l_G)->GCdebt > 0) { ((ci->u.l.savedpc = pc), L->top.p = (L->top.p)); luaC_step(L); (trap = ci->u.l.trap);}; ((void)0); }; {((void) 0); ((void) 0);}; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_CLOSE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaF_close(L, ra, 0, 1)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_TBC: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));

        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaF_newtbcupval(L, ra)));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_JMP: {
        { pc += ((((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 0; (trap = ci->u.l.trap); };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_EQ: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int cond;
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (cond = luaV_equalobj(L, (&(ra)->val), rb)), (trap = ci->u.l.trap));
        if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };;
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LT: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); int cond; TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); if ((((((&(ra)->val)))->tt_) == (((3) | ((0) << 4)))) && ((((rb))->tt_) == (((3) | ((0) << 4))))) { lua_Integer ia = ((((&(ra)->val))->value_).i); lua_Integer ib = (((rb)->value_).i); cond = (ia < ib); } else if (((((((((&(ra)->val)))->tt_)) & 0x0F)) == (3)) && (((((((rb))->tt_)) & 0x0F)) == (3))) cond = LTnum((&(ra)->val), rb); else (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (cond = lessthanothers(L, (&(ra)->val), rb)), (trap = ci->u.l.trap)); if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LE: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); int cond; TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val); if ((((((&(ra)->val)))->tt_) == (((3) | ((0) << 4)))) && ((((rb))->tt_) == (((3) | ((0) << 4))))) { lua_Integer ia = ((((&(ra)->val))->value_).i); lua_Integer ib = (((rb)->value_).i); cond = (ia <= ib); } else if (((((((((&(ra)->val)))->tt_)) & 0x0F)) == (3)) && (((((((rb))->tt_)) & 0x0F)) == (3))) cond = LEnum((&(ra)->val), rb); else (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (cond = lessequalothers(L, (&(ra)->val), rb)), (trap = ci->u.l.trap)); if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_EQK: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = (k+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0))))))));

        int cond = luaV_equalobj(
# 1625 "lvm.c" 3 4
                  ((void *)0)
# 1625 "lvm.c"
                  ,(&(ra)->val),rb);
        if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };;
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_EQI: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int cond;
        int im = ((((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1));
        if ((((((&(ra)->val)))->tt_) == (((3) | ((0) << 4)))))
          cond = (((((&(ra)->val))->value_).i) == im);
        else if ((((((&(ra)->val)))->tt_) == (((3) | ((1) << 4)))))
          cond = ((((((&(ra)->val))->value_).n))==(((lua_Number)((im)))));
        else
          cond = 0;
        if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };;
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LTI: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); int cond; int im = ((((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1)); if ((((((&(ra)->val)))->tt_) == (((3) | ((0) << 4))))) cond = (((((&(ra)->val))->value_).i) < im); else if ((((((&(ra)->val)))->tt_) == (((3) | ((1) << 4))))) { lua_Number fa = ((((&(ra)->val))->value_).n); lua_Number fim = ((lua_Number)((im))); cond = ((fa)<(fim)); } else { int isf = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (cond = luaT_callorderiTM(L, (&(ra)->val), im, 0, isf, TM_LT)), (trap = ci->u.l.trap)); } if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_LEI: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); int cond; int im = ((((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1)); if ((((((&(ra)->val)))->tt_) == (((3) | ((0) << 4))))) cond = (((((&(ra)->val))->value_).i) <= im); else if ((((((&(ra)->val)))->tt_) == (((3) | ((1) << 4))))) { lua_Number fa = ((((&(ra)->val))->value_).n); lua_Number fim = ((lua_Number)((im))); cond = ((fa)<=(fim)); } else { int isf = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (cond = luaT_callorderiTM(L, (&(ra)->val), im, 0, isf, TM_LE)), (trap = ci->u.l.trap)); } if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_GTI: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); int cond; int im = ((((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1)); if ((((((&(ra)->val)))->tt_) == (((3) | ((0) << 4))))) cond = (((((&(ra)->val))->value_).i) > im); else if ((((((&(ra)->val)))->tt_) == (((3) | ((1) << 4))))) { lua_Number fa = ((((&(ra)->val))->value_).n); lua_Number fim = ((lua_Number)((im))); cond = ((fa)>(fim)); } else { int isf = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (cond = luaT_callorderiTM(L, (&(ra)->val), im, 1, isf, TM_LT)), (trap = ci->u.l.trap)); } if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_GEI: {
        { StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); int cond; int im = ((((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))) - (((1<<8)-1) >> 1)); if ((((((&(ra)->val)))->tt_) == (((3) | ((0) << 4))))) cond = (((((&(ra)->val))->value_).i) >= im); else if ((((((&(ra)->val)))->tt_) == (((3) | ((1) << 4))))) { lua_Number fa = ((((&(ra)->val))->value_).n); lua_Number fim = ((lua_Number)((im))); cond = ((fa)>=(fim)); } else { int isf = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (cond = luaT_callorderiTM(L, (&(ra)->val), im, 1, isf, TM_LE)), (trap = ci->u.l.trap)); } if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_TEST: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int cond = !((((((&(ra)->val)))->tt_) == (((1) | ((0) << 4)))) || ((((((((&(ra)->val)))->tt_)) & 0x0F)) == (0)));
        if (cond != ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0)))))))) pc++; else { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };;
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_TESTSET: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        TValue *rb = (&((base+((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))))))->val);
        if ((((((rb))->tt_) == (((1) | ((0) << 4)))) || (((((((rb))->tt_)) & 0x0F)) == (0))) == ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<(1)))<<(0))))))))
          pc++;
        else {
          { TValue *io1=((&(ra)->val)); const TValue *io2=(rb); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
          { Instruction ni = *pc; { pc += ((((int)((((ni)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0)))))) - (((1 << ((8 + 8 + 1) + 8)) - 1) >> 1)) + 1; (trap = ci->u.l.trap); }; };
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_CALL: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        CallInfo *newci;
        int b = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int nresults = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) - 1;
        if (b != 0)
          L->top.p = ra + b;

        (ci->u.l.savedpc = pc);
        if ((newci = luaD_precall(L, ra, nresults)) == 
# 1684 "lvm.c" 3 4
                                                      ((void *)0)
# 1684 "lvm.c"
                                                          )
          (trap = ci->u.l.trap);
        else {
          ci = newci;
          goto startfunc;
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_TAILCALL: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int b = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int n;
        int nparams1 = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));

        int delta = (nparams1) ? ci->u.l.nextraargs + nparams1 : 0;
        if (b != 0)
          L->top.p = ra + b;
        else
          b = ((int)((L->top.p - ra)));
        (ci->u.l.savedpc = pc);
        if (((((int)((((i) & (1u << ((0 + 7) + 8))))))))) {
          luaF_closeupval(L, base);
          ((void)0);
          ((void)0);
        }
        if ((n = luaD_pretailcall(L, ci, ra, b, delta)) < 0)
          goto startfunc;
        else {
          ci->func.p -= delta;
          luaD_poscall(L, ci, n);
          (trap = ci->u.l.trap);
          goto ret;
        }
      }
      L_OP_RETURN: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int n = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) - 1;
        int nparams1 = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        if (n < 0)
          n = ((int)((L->top.p - ra)));
        (ci->u.l.savedpc = pc);
        if (((((int)((((i) & (1u << ((0 + 7) + 8))))))))) {
          ci->u2.nres = n;
          if (L->top.p < ci->top.p)
            L->top.p = ci->top.p;
          luaF_close(L, base, (-1), 1);
          (trap = ci->u.l.trap);
          { if ((__builtin_expect(((trap) != 0), 0))) { (base = ci->func.p + 1); ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); } };
        }
        if (nparams1)
          ci->func.p -= ci->u.l.nextraargs + nparams1;
        L->top.p = ra + n;
        luaD_poscall(L, ci, n);
        (trap = ci->u.l.trap);
        goto ret;
      }
      L_OP_RETURN0: {
        if ((__builtin_expect(((L->hookmask) != 0), 0))) {
          StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
          L->top.p = ra;
          (ci->u.l.savedpc = pc);
          luaD_poscall(L, ci, 0);
          trap = 1;
        }
        else {
          int nres;
          L->ci = ci->previous;
          L->top.p = base - 1;
          for (nres = ci->nresults; (__builtin_expect(((nres > 0) != 0), 0)); nres--)
            (((&(L->top.p++)->val))->tt_=(((0) | ((0) << 4))));
        }
        goto ret;
      }
      L_OP_RETURN1: {
        if ((__builtin_expect(((L->hookmask) != 0), 0))) {
          StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
          L->top.p = ra + 1;
          (ci->u.l.savedpc = pc);
          luaD_poscall(L, ci, 1);
          trap = 1;
        }
        else {
          int nres = ci->nresults;
          L->ci = ci->previous;
          if (nres == 0)
            L->top.p = base - 1;
          else {
            StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
            { TValue *io1=((&(base - 1)->val)); const TValue *io2=((&(ra)->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
            L->top.p = base;
            for (; (__builtin_expect(((nres > 1) != 0), 0)); nres--)
              (((&(L->top.p++)->val))->tt_=(((0) | ((0) << 4))));
          }
        }
       ret:
        if (ci->callstatus & (1<<2))
          return;
        else {
          ci = ci->previous;
          goto returning;
        }
      }
      L_OP_FORLOOP: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        if ((((((&(ra + 2)->val)))->tt_) == (((3) | ((0) << 4))))) {
          lua_Unsigned count = ((lua_Unsigned)(((((&(ra + 1)->val))->value_).i)));
          if (count > 0) {
            lua_Integer step = ((((&(ra + 2)->val))->value_).i);
            lua_Integer idx = ((((&(ra)->val))->value_).i);
            { TValue *io=((&(ra + 1)->val)); ((void)0); ((io)->value_).i=(count - 1); };
            idx = ((lua_Integer)(((lua_Unsigned)(idx)) + ((lua_Unsigned)(step))));
            { TValue *io=((&(ra)->val)); ((void)0); ((io)->value_).i=(idx); };
            { TValue *io=((&(ra + 3)->val)); ((io)->value_).i=(idx); ((io)->tt_=(((3) | ((0) << 4)))); };
            pc -= ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))));
          }
        }
        else if (floatforloop(ra))
          pc -= ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))));
        (trap = ci->u.l.trap);
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_FORPREP: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        ((ci->u.l.savedpc = pc), L->top.p = ci->top.p);
        if (forprep(L, ra))
          pc += ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0))))))) + 1;
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_TFORPREP: {
       StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));

        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaF_newtbcupval(L, ra + 3)));
        pc += ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))));
        i = *(pc++);
        ((void)0);
        goto l_tforcall;
      }
      L_OP_TFORCALL: {
       l_tforcall: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));






        memcpy(ra + 4, ra, 3 * sizeof(*ra));
        L->top.p = ra + 4 + 3;
        ((ci->u.l.savedpc = pc), (luaD_call(L, ra + 4, ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))))), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { (base = ci->func.p + 1); ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0))))))); } };
        i = *(pc++);
        ((void)0);
        goto l_tforloop;
      }}
      L_OP_TFORLOOP: {
       l_tforloop: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        if (!((((((((&(ra + 4)->val)))->tt_)) & 0x0F)) == (0))) {
          { TValue *io1=((&(ra + 2)->val)); const TValue *io2=((&(ra + 4)->val)); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
          pc -= ((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))));
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }}
      L_OP_SETLIST: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int n = ((((int)((((i)>>((((0 + 7) + 8) + 1))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        unsigned int last = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        Table *h = ((&((((union GCUnion *)(((((&(ra)->val))->value_).gc))))->h)));
        if (n == 0)
          n = ((int)((L->top.p - ra))) - 1;
        else
          L->top.p = ci->top.p;
        last += n;
        if (((((int)((((i) & (1u << ((0 + 7) + 8))))))))) {
          last += ((((int)((((*pc)>>((0 + 7))) & ((~((~(Instruction)0)<<(((8 + 8 + 1) + 8))))<<(0))))))) * (((1<<8)-1) + 1);
          pc++;
        }
        if (last > luaH_realasize(h))
          luaH_resizearray(L, h, last);
        for (; n > 0; n--) {
          TValue *val = (&(ra + n)->val);
          { TValue *io1=(&h->array[last - 1]); const TValue *io2=(val); io1->value_ = io2->value_; ((io1)->tt_=(io2->tt_)); ((void)L, ((void)0)); ((void)0); };
          last--;
          ( (((val)->tt_) & (1 << 6)) ? ( (((((&(((union GCUnion *)((h)))->gc)))->marked) & ((1<<(5)))) && ((((((val)->value_).gc))->marked) & (((1<<(3)) | (1<<(4)))))) ? luaC_barrierback_(L,(&(((union GCUnion *)((h)))->gc))) : ((void)((0)))) : ((void)((0))));
        }
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_CLOSURE: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        Proto *p = cl->p->p[((((int)((((i)>>(((0 + 7) + 8))) & ((~((~(Instruction)0)<<((8 + 8 + 1))))<<(0)))))))];
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (pushclosure(L, p, cl->upvals, base, ra)));
        { { if ((L->l_G)->GCdebt > 0) { ((ci->u.l.savedpc = pc), L->top.p = (ra + 1)); luaC_step(L); (trap = ci->u.l.trap);}; ((void)0); }; {((void) 0); ((void) 0);}; };
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_VARARG: {
        StkId ra = (base+(((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))));
        int n = ((((int)((((i)>>(((((0 + 7) + 8) + 1) + 8))) & ((~((~(Instruction)0)<<(8)))<<(0))))))) - 1;
        (((ci->u.l.savedpc = pc), L->top.p = ci->top.p), (luaT_getvarargs(L, ci, ra, n)), (trap = ci->u.l.trap));
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_VARARGPREP: {
        ((ci->u.l.savedpc = pc), (luaT_adjustvarargs(L, (((int)((((i)>>((0 + 7))) & ((~((~(Instruction)0)<<(8)))<<(0)))))), ci, cl->p)), (trap = ci->u.l.trap));
        if ((__builtin_expect(((trap) != 0), 0))) {
          luaD_hookcall(L, ci);
          L->oldpc = 1;
        }
        (base = ci->func.p + 1);
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
      L_OP_EXTRAARG: {
        ((void)0);
        { if ((__builtin_expect(((trap) != 0), 0))) { trap = luaG_traceexec(L, pc); (base = ci->func.p + 1); } i = *(pc++); }; goto *disptab[(((OpCode)(((i)>>0) & ((~((~(Instruction)0)<<(7)))<<(0)))))];;;
      }
    }
  }
}
