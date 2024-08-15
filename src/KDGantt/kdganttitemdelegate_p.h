/****************************************************************************
**
** This file is part of the KD Chart library.
**
** SPDX-FileCopyrightText: 2001 Klarälvdalens Datakonsult AB, a KDAB Group company <info@kdab.com>
**
** SPDX-License-Identifier: MIT
**
****************************************************************************/

#ifndef KDGANTTITEMDELEGATE_P_H
#define KDGANTTITEMDELEGATE_P_H

#include "kdganttitemdelegate.h"

#include <QHash>

namespace KDGantt {
class ItemDelegate::Private
{
public:
    Private();

    QPen constraintPen(const QPointF &start, const QPointF &end, const Constraint &constraint);

    QHash<ItemType, QBrush> defaultbrush;
    QHash<ItemType, QPen> defaultpen;

    QHash<TaskStatus, QBrush> customizeddefaultbrush;
    QHash<TaskStatus, QPen> customizeddefaultpen;
};
}

#endif /* KDGANTTITEMDELEGATE_P_H */
