// python-wrapper for liblxi
// liblxi: https://github.com/lxi-tools/liblxi
// python-liblxi: https://github.com/lxi-tools/python-liblxi
//
// python-liblxi is available for use under the 3-clause (or "modified") BSD
// license, see COPYING
//
// Anders E.E. Wallin, 2018

#include <boost/python.hpp>

#include "lxi.h"

namespace bp = boost::python;

BOOST_PYTHON_MODULE(liblxi) {
    /* API from readme
    int lxi_init(void);
    int lxi_discover(struct lxi_info_t *info, int timeout, lxi_discover_t type);
    int lxi_connect(const char *address, int port, const char *name, int timeout, lxi_protocol_t protocol);
    int lxi_send(int device, const char *message, int length, int timeout);
    int lxi_receive(int device, char *message, int length, int timeout);
    int lxi_disconnect(int device);
    */
    bp::def("init", lxi_init);
    bp::def("discover", lxi_discover);
    bp::def("connect", lxi_connect);
    bp::def("send", lxi_send);
    bp::def("receive", lxi_receive);
    bp::def("disconnect", lxi_disconnect);

    bp::enum_<lxi_discover_t>("DiscoverType")
        .value("VXI11", DISCOVER_VXI11)   
        .value("MDNS", DISCOVER_MDNS)
    ;
    bp::enum_<lxi_protocol_t>("ProtocolType")
        .value("VXI11", VXI11)
        .value("RAW", RAW)
        .value("HISLIP", HISLIP)
    ;

}
